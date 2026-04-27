import copy
from datetime import datetime, timedelta

import pandas as pd

from utils.metabase import tarik_metabase, get_token
from utils.gsheet import read_sheet
from config.settings import METABASE_CONFIG, GSHEET


def get_previous_month_period():
    today = datetime.today()
    first_day_this_month = today.replace(day=1)
    last_day_prev_month = first_day_this_month - timedelta(days=1)
    first_day_prev_month = last_day_prev_month.replace(day=1)

    return (
        first_day_prev_month.strftime("%Y-%m-%d"),
        last_day_prev_month.strftime("%Y-%m-%d"),
    )


def render_params(param_templates, runtime_values):
    rendered = []

    for param in param_templates:
        p = copy.deepcopy(param)

        # preferred style: value_key
        if "value_key" in p:
            key = p.pop("value_key")
            if key not in runtime_values:
                raise KeyError(f"runtime_values tidak punya key: {key}")
            p["value"] = runtime_values[key]

        # compatibility style: value = "start_date" / "b2b_cc" / etc
        elif isinstance(p.get("value"), str) and p["value"] in runtime_values:
            p["value"] = runtime_values[p["value"]]

        rendered.append(p)

    return rendered


def build_shipper_lists():
    print("\n[1/5] Read Google Sheet key_shipper...")

    df = read_sheet(
        GSHEET["key_shipper"]["sheet_id"],
        GSHEET["key_shipper"]["tabs"]["main"],
    )

    print(f"Key shipper shape: {df.shape}")
    print("Columns:", df.columns.tolist())

    required_cols = ["Type", "Shipper ID"]
    missing_cols = [c for c in required_cols if c not in df.columns]
    if missing_cols:
        raise ValueError(f"Kolom tidak ditemukan di sheet key_shipper: {missing_cols}")

    df["Type"] = df["Type"].astype(str).str.strip()

    b2b_cc_categories = [
        "B2C Cold Chain Sameday",
        "B2C Cold Chain Next Day",
        "B2B Dry Reguler",
        "B2B Sameday Reguler",
        "B2B Sameday Premium",
    ]

    fsbd_categories = [
        "FSBD Key Shipper",
        "Aggregator Keyshipper",
    ]

    bd_categories = [
        "FSBD Key Shipper"
    ]

    b2b_cc_list = (
        pd.to_numeric(df[df["Type"].isin(b2b_cc_categories)]["Shipper ID"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
        .drop_duplicates()
        .tolist()
    )

    fsbd_list = (
        pd.to_numeric(df[df["Type"].isin(fsbd_categories)]["Shipper ID"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
        .drop_duplicates()
        .tolist()
    )

    bd_list = (
        pd.to_numeric(df[df["Type"].isin(bd_categories)]["Shipper ID"], errors="coerce")
        .dropna()
        .astype(int)
        .astype(str)
        .drop_duplicates()
        .tolist()
    )

    print(f"Total b2b_cc_list: {len(b2b_cc_list)} | sample: {b2b_cc_list[:5]}")
    print(f"Total fsbd_list: {len(fsbd_list)} | sample: {fsbd_list[:5]}")
    print(f"Total fsbd_list: {len(bd_list)} | sample: {bd_list[:5]}")

    return b2b_cc_list, fsbd_list, bd_list


def build_runtime_from_param_table(
    df: pd.DataFrame,
    segment_col: str,
    filter_col: str = "Filter Name",
) -> dict:
    """
    Param table format:
    Filter Name | B2BR | FSBD | Tiktok
    """
    df.columns = df.columns.astype(str).str.strip()

    required_cols = [filter_col, segment_col]
    missing_cols = [c for c in required_cols if c not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Kolom param tidak ditemukan: {missing_cols}. "
            f"Kolom tersedia: {df.columns.tolist()}"
        )

    work = df[[filter_col, segment_col]].copy()
    work[filter_col] = work[filter_col].astype(str).str.strip()
    work = work[work[filter_col] != ""]

    runtime = {}

    for _, row in work.iterrows():
        key = row[filter_col]
        raw_val = row[segment_col]

        if pd.isna(raw_val) or str(raw_val).strip() == "":
            runtime[key] = None
            continue

        try:
            num = float(raw_val)
            runtime[key] = int(num) if num.is_integer() else num
        except ValueError:
            runtime[key] = str(raw_val).strip()

    return runtime


def build_poh_runtime_by_segment():
    print("\n[2/5] Read POH parameter table...")

    df_poh = read_sheet(
        GSHEET["param_metabase"]["sheet_id"],
        GSHEET["param_metabase"]["tabs"]["param_poh_type_shipper"],
    )

    print(f"POH param shape: {df_poh.shape}")
    print("POH columns:", df_poh.columns.tolist())

    return {
        "poh_b2b_cc": build_runtime_from_param_table(df_poh, "B2BR"),
        "poh_fsbd": build_runtime_from_param_table(df_poh, "FSBD"),
        "poh_tiktok": build_runtime_from_param_table(df_poh, "Tiktok"),
    }


def run_report(report_key, runtime_values, token, segment_key=None):
    cfg = METABASE_CONFIG["fm"][report_key]

    common_params = render_params(
        cfg["common_params_template"],
        runtime_values,
    )

    segment_params = []
    if segment_key is not None:
        segment_params = render_params(
            cfg["shipper_params_template"][segment_key],
            runtime_values,
        )

    final_params = common_params + segment_params
    desc = f"{report_key}_{segment_key}" if segment_key else report_key

    print(f"\n[RUN] {desc}")
    print(f"URL: {cfg['url']}")
    print(f"Total params: {len(final_params)}")

    df_result = tarik_metabase(
        url=cfg["url"],
        parameters=final_params,
        token=token,
        desc=desc,
    )

    print(f"{desc} shape: {df_result.shape}")

    if df_result.empty:
        print(f"WARNING: {desc} hasil kosong")
    else:
        print(df_result.head(5).to_string(index=False))

    return df_result


def should_skip_report(report_key):
    cfg = METABASE_CONFIG["fm"][report_key]
    url = cfg.get("url", "")
    return not url or "PASTE_" in url


def build_driver_list():
    print("\n[2/5] Read Driver List from param_metabase...")

    df = read_sheet(
        GSHEET["param_metabase"]["sheet_id"],
        GSHEET["param_metabase"]["tabs"]["param_driver_type"],  # pastikan key ini ada di settings
    )

    df.columns = df.columns.astype(str).str.strip()

    required_cols = ["Function", "Driver Type"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(
            f"Kolom tidak ditemukan di Driver Type sheet: {missing}. "
            f"Available: {df.columns.tolist()}"
        )

    # ✅ ambil hanya FM
    df_fm = df[df["Function"].astype(str).str.strip() == "FM"]

    driver_list = (
        df_fm["Driver Type"]
        .dropna()
        .astype(str)
        .str.strip()
        .loc[lambda s: s != ""]
        .drop_duplicates()
        .tolist()
    )

    print(f"Total driver_list: {len(driver_list)} | sample: {driver_list[:5]}")

    return driver_list

def build_hub_whitelist():
    print("\n[2/5] Read Hub Whitelist ITV from param_metabase...")

    df = read_sheet(
        GSHEET["param_metabase"]["sheet_id"],
        GSHEET["param_metabase"]["tabs"]["param_whitelist_hub_itv"],
    )

    df.columns = df.columns.astype(str).str.strip()

    required_cols = ["Description", "Hub Name"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(
            f"Kolom tidak ditemukan di Whitelist Hub ITV: {missing}. "
            f"Available: {df.columns.tolist()}"
        )

    df["Description"] = df["Description"].astype(str).str.strip()

    def get_list(desc):
        result = (
            df[df["Description"].eq(desc)]["Hub Name"]
            .dropna()
            .astype(str)
            .str.strip()
            .loc[lambda s: s != ""]
            .drop_duplicates()
            .tolist()
        )

        if not result:
            print(f"WARNING: {desc} list kosong!")

        print(f"Total {desc}: {len(result)} | sample: {result[:5]}")
        return result

    return {
        "hub_whitelist1": get_list("Whitelist Hub1"),
        "hub_whitelist2": get_list("Whitelist Hub2"),
    }


def run():
    print("=== FM DAY 2 START ===")

    start_date, end_date = get_previous_month_period()
    print(f"\n[0/5] Period: {start_date} to {end_date}")

    print("\n[1/5] Get Metabase token...")
    token = get_token()
    print("Token loaded:", bool(token))

    b2b_cc_list, fsbd_list, bd_list = build_shipper_lists()
    poh_runtime_map = build_poh_runtime_by_segment()
    driver_list = build_driver_list()
    hub_whitelist = build_hub_whitelist()

    base_runtime_values = {
        "start_date": start_date,
        "end_date": end_date,
        "b2b_cc": b2b_cc_list,
        "fsbd": fsbd_list,
        "bd_shipper": bd_list,
        "driver_list": driver_list,
        "hub_whitelist1": hub_whitelist["hub_whitelist1"],
        "hub_whitelist2": hub_whitelist["hub_whitelist2"],
        "period_str": f"{start_date}~{end_date}",
    }

    results = {}

    # report yang sekarang sudah beneran kamu isi
    fm_report_plan = [
        {"report_key": "poh_b2b_cc", "poh_runtime_key": "poh_b2b_cc"},
        {"report_key": "poh_fsbd", "poh_runtime_key": "poh_fsbd"},
        {"report_key": "poh_tiktok", "poh_runtime_key": "poh_tiktok"},
        {"report_key": "no_success_rate_shopee_laz_tt_bd"},
        {"report_key": "no_rsvn_completed_key_shipper"},
    ]

    print("\n[4/5] Pull FM Metabase reports...")

    for item in fm_report_plan:
        report_key = item["report_key"]

        if report_key not in METABASE_CONFIG["fm"]:
            print(f"SKIP {report_key}: tidak ada di METABASE_CONFIG['fm']")
            continue

        if should_skip_report(report_key):
            print(f"SKIP {report_key}: URL masih placeholder")
            continue

        runtime_values = base_runtime_values.copy()

        # inject POH parameter sesuai kolom B2BR / FSBD / Tiktok
        if "poh_runtime_key" in item:
            runtime_values.update(poh_runtime_map[item["poh_runtime_key"]])

        results[report_key] = run_report(
            report_key=report_key,
            runtime_values=runtime_values,
            token=token,
        )

    print("\n[5/5] Summary result shapes:")
    for key, df in results.items():
        print(f"- {key}: {df.shape}")

    print("\n=== FM DAY 2 DONE ===")

    return results


if __name__ == "__main__":
    run()
