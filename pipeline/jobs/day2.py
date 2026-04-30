import copy
from datetime import datetime, timedelta

import pandas as pd

from utils.metabase import tarik_metabase, get_token
from utils.gsheet import read_sheet
from config.settings import METABASE_CONFIG, GSHEET
from utils.gsheet import read_sheet, write_sheet
from utils.transform import (
    pivot_assignment_streamline,
    pivot_assignment_inaccuracy_user,
    pivot_rsvn_completed,
    pivot_n0_attempt_rate,
    pivot_rot,
    pivot_poh,
    pivot_popa_validity,
    pivot_sr_rts,
    select_lnd,
    select_itv,
    pivot_4w_productivity,
)



def get_previous_month_period():
    today = datetime.today()
    first_day_this_month = today.replace(day=1)
    last_day_prev_month = first_day_this_month - timedelta(days=1)
    first_day_prev_month = last_day_prev_month.replace(day=1)

    return (
        first_day_prev_month.strftime("%Y-%m-%d"),
        last_day_prev_month.strftime("%Y-%m-%d"),
    )


def normalize_scalar(value):
    if value is None:
        return None

    try:
        if pd.isna(value):
            return None
    except Exception:
        pass

    text = str(value).strip()
    if text == "":
        return None

    try:
        num = float(text)
        return int(num) if num.is_integer() else num
    except ValueError:
        return text


def render_params(param_templates, runtime_values):
    rendered = []

    for param in param_templates:
        p = copy.deepcopy(param)

        if "value_key" in p:
            key = p.pop("value_key")
            if key not in runtime_values:
                raise KeyError(f"runtime_values tidak punya key: {key}")
            p["value"] = runtime_values[key]

        elif isinstance(p.get("value"), str) and p["value"] in runtime_values:
            p["value"] = runtime_values[p["value"]]

        rendered.append(p)

    return rendered


def get_column_name(df: pd.DataFrame, candidates: list[str]) -> str:
    normalized = {str(col).strip().lower(): col for col in df.columns}
    for candidate in candidates:
        key = candidate.strip().lower()
        if key in normalized:
            return normalized[key]

    raise ValueError(
        f"Kolom tidak ditemukan. Candidates={candidates}, available={df.columns.tolist()}"
    )


def build_sheet_value_list(sheet_id: str, tab_name: str) -> list:
    df = read_sheet(sheet_id, tab_name)
    print(f"{tab_name} shape: {df.shape}")
    print(f"{tab_name} columns: {df.columns.tolist()}")

    value_col = get_column_name(df, ["Value"])
    values = [normalize_scalar(v) for v in df[value_col].tolist()]
    values = [v for v in values if v is not None]

    return values


def build_shipper_lists():
    print("\n[1/8] Read Google Sheet key_shipper...")

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

    def extract_shipper_ids(mask):
        s = (
            df.loc[mask, "Shipper ID"]
            .dropna()
            .astype(str)
            .str.strip()
            .str.replace(r"\.0$", "", regex=True)
        )

        s = s[(s != "") & (s.str.lower() != "nan")]

        return s.drop_duplicates().tolist()

    b2b_cc_list = extract_shipper_ids(df["Type"].isin(b2b_cc_categories))
    fsbd_list = extract_shipper_ids(df["Type"].str.contains("fsbd|aggregator", case=False, na=False))
    aggregator_list = extract_shipper_ids(df["Type"].str.contains("aggregator", case=False, na=False))
    bd_list = extract_shipper_ids(df["Type"].str.contains("fsbd", case=False, na=False))

    print(f"Total b2b_cc_list: {len(b2b_cc_list)} | sample: {b2b_cc_list[:5]}")
    print(f"Total fsbd_list: {len(fsbd_list)} | sample: {fsbd_list[:5]}")
    print(f"Total aggregator_list: {len(aggregator_list)} | sample: {aggregator_list[:5]}")
    print(f"Total bd_list: {len(bd_list)} | sample: {bd_list[:5]}")

    return b2b_cc_list, fsbd_list, aggregator_list, bd_list


def build_runtime_from_param_table(
    df: pd.DataFrame,
    segment_col: str,
    filter_col: str = "Filter Name",
) -> dict:
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
        runtime[key] = normalize_scalar(raw_val)

    return runtime


def build_poh_runtime_by_segment():
    print("\n[2/8] Read POH parameter table...")

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


def build_driver_list():
    print("\n[3/8] Read Driver Type...")

    df = read_sheet(
        GSHEET["param_metabase"]["sheet_id"],
        GSHEET["param_metabase"]["tabs"]["param_driver_type"],
    )

    df.columns = df.columns.astype(str).str.strip()

    required_cols = ["Function", "Driver Type"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(
            f"Kolom tidak ditemukan di Driver Type sheet: {missing}. "
            f"Available: {df.columns.tolist()}"
        )

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
    print("\n[4/8] Read Hub Whitelist ITV...")

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
        print(f"Total {desc}: {len(result)} | sample: {result[:5]}")
        return result

    return {
        "hub_whitelist1": get_list("Whitelist Hub1"),
        "hub_whitelist2": get_list("Whitelist Hub2"),
    }


def build_cutoff_runtime():
    print("\n[5/8] Read Cutoff params...")

    values = build_sheet_value_list(
        GSHEET["param_metabase"]["sheet_id"],
        GSHEET["param_metabase"]["tabs"]["param_cutoff"],
    )

    if len(values) < 5:
        raise ValueError(f"Cutoff values kurang dari 5 row: {values}")

    runtime = {
        "base_cutoff": values[2],
        "cutoff1": values[3],
        "cutoff2": values[4],
    }

    print("Cutoff runtime:", runtime)
    return runtime


def build_assignment_runtime():
    print("\n[6/8] Read Assignment params...")

    df = read_sheet(
        GSHEET["param_metabase"]["sheet_id"],
        GSHEET["param_metabase"]["tabs"]["param_assignment"],
    )

    print(f"Assignment shape: {df.shape}")
    print(f"Assignment columns: {df.columns.tolist()}")

    key_col = get_column_name(df, ["Filter Name", "Parameter"])
    value_col = get_column_name(df, ["Value"])

    runtime = {}
    for _, row in df[[key_col, value_col]].iterrows():
        key = str(row[key_col]).strip()
        if not key:
            continue
        runtime[key] = normalize_scalar(row[value_col])

    expected_keys = [
        "lt_hour_scheduled_cutoff_1",
        "lt_hour_scheduled_cutoff_2",
        "lt_hour_scheduled_cutoff_3",
        "lt_hour_scheduled_cutoff_4",
        "lt_hour_after_creation_cutoff_1",
        "lt_hour_after_creation_cutoff_2",
        "lt_hour_after_creation_cutoff_3",
        "lt_hour_after_creation_cutoff_4",
        "start_rsvn_creation_cutoff_1",
        "start_rsvn_creation_cutoff_2",
        "start_rsvn_creation_cutoff_3",
        "start_rsvn_creation_cutoff_4",
        "end_rsvn_creation_cutoff_1",
        "end_rsvn_creation_cutoff_2",
        "end_rsvn_creation_cutoff_3",
        "end_rsvn_creation_cutoff_4",
        "lt_type_cutoff_1",
        "lt_type_cutoff_2",
        "lt_type_cutoff_3",
        "lt_type_cutoff_4",
        "lt_grace_period_day_cutoff_1",
        "lt_grace_period_day_cutoff_2",
        "lt_grace_period_day_cutoff_3",
        "lt_grace_period_day_cutoff_4",
    ]

    missing = [k for k in expected_keys if k not in runtime]
    if missing:
        raise ValueError(f"Assignment param belum lengkap, missing keys: {missing}")

    print("Assignment runtime sample:", {k: runtime[k] for k in expected_keys[:4]})
    return runtime


def build_target_runtime():
    print("\n[7/8] Read Target params...")

    values = build_sheet_value_list(
        GSHEET["param_metabase"]["sheet_id"],
        GSHEET["param_metabase"]["tabs"]["param_target"],
    )

    keys = [
        "4w_gj_target",
        "4w_wj_target",
        "4w_cj_target",
        "4w_ej_target",
        "2w_gj_target",
        "2w_wj_target",
        "2w_cj_target",
        "2w_ej_target",
        "target_value",
    ]

    if len(values) < len(keys):
        raise ValueError(f"Target values kurang. Expected {len(keys)}, got {len(values)}")

    runtime = dict(zip(keys, values[:len(keys)]))
    runtime["target_pdv"] = runtime["target_value"]

    print("Target runtime:", runtime)
    return runtime


def build_address_id_list():
    print("\n[8/8] Read Exclude Address...")

    df = read_sheet(
        GSHEET["param_metabase"]["sheet_id"],
        GSHEET["param_metabase"]["tabs"]["param_exclude_address"],
    )

    print(f"Exclude Address shape: {df.shape}")
    print(f"Exclude Address columns: {df.columns.tolist()}")

    address_col = get_column_name(df, ["Address ID"])

    address_id_list = (
        pd.to_numeric(df[address_col], errors="coerce")
        .dropna()
        .astype(int)
        .drop_duplicates()
        .tolist()
    )

    if not address_id_list:
        print("WARNING: ADDRESS_ID list kosong!")

    print(f"total address_id: {len(address_id_list)}")
    print(f"address_id_list sample: {address_id_list[:5]}")

    return address_id_list


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


def run():
    print("=== FM DAY 2 START ===")

    start_date, end_date = get_previous_month_period()
    period_str = f"{start_date}~{end_date}"
    print(f"\n[0/8] Period: {start_date} to {end_date}")

    print("\n[1/8] Get Metabase token...")
    token = get_token()
    print("Token loaded:", bool(token))

    b2b_cc_list, fsbd_list, aggregator_list, bd_list = build_shipper_lists()
    poh_runtime_map = build_poh_runtime_by_segment()
    driver_list = build_driver_list()
    hub_whitelist = build_hub_whitelist()
    cutoff_runtime = build_cutoff_runtime()
    assignment_runtime = build_assignment_runtime()
    target_runtime = build_target_runtime()
    address_id_list = build_address_id_list()

    base_runtime_values = {
        "start_date": start_date,
        "end_date": end_date,
        "period_str": period_str,
        "start_end": start_date,
        "end_end": end_date,
        "b2b_cc": b2b_cc_list,
        "fsbd": fsbd_list,
        "bd_shipper": bd_list,
        "aggregator": aggregator_list,
        "driver_list": driver_list,
        "driver_type": driver_list,
        "hub_whitelist1": hub_whitelist["hub_whitelist1"],
        "hub_whitelist2": hub_whitelist["hub_whitelist2"],
        "address_id_list": address_id_list,
        **cutoff_runtime,
        **assignment_runtime,
        **target_runtime,
    }

    results = {}

    fm_report_plan = [
        {"report_key": "poh_b2b_cc", "runtime_patch_key": "poh_b2b_cc"},
        {"report_key": "poh_fsbd", "runtime_patch_key": "poh_fsbd"},
        {"report_key": "poh_tiktok", "runtime_patch_key": "poh_tiktok"},
        {"report_key": "no_success_rate_shopee_laz_tt_bd"},
        {"report_key": "no_rsvn_completed_b2b_cc"},
        {"report_key": "no_attempt_rate_key_shipper"},
        {"report_key": "pst_itv", "segment_key": "b2b_cc"},
        {"report_key": "pst_itv", "segment_key": "fsbd"},
        # {"report_key": "rot"},
        # {"report_key": "lnd"},
        # {"report_key": "popa_validity", "segment_key": "lazada"},
        # {"report_key": "popa_validity", "segment_key": "aggregator"},
        # {"report_key": "popa_validity", "segment_key": "fsbd_lazada"},
        # {"report_key": "assign_inaccuracy"},
        # {"report_key": "assign_streamline"},
        # {"report_key": "four_w_productivity"},
    ]

    print("\n[FINAL] Pull FM Metabase reports...")

    for item in fm_report_plan:
        report_key = item["report_key"]
        segment_key = item.get("segment_key")

        if report_key not in METABASE_CONFIG["fm"]:
            print(f"SKIP {report_key}: tidak ada di METABASE_CONFIG['fm']")
            continue

        if should_skip_report(report_key):
            print(f"SKIP {report_key}: URL masih placeholder")
            continue

        runtime_values = base_runtime_values.copy()

        if "runtime_patch_key" in item:
            runtime_values.update(poh_runtime_map[item["runtime_patch_key"]])

        result_name = f"{report_key}_{segment_key}" if segment_key else report_key

        results[result_name] = run_report(
            report_key=report_key,
            runtime_values=runtime_values,
            token=token,
            segment_key=segment_key,
        )

    print("\nSummary result shapes:")
    for key, df in results.items():
        print(f"- {key}: {df.shape}")

    print("\n[TRANSFORM] Build final outputs...")
    final_outputs = {}

    if "poh_b2b_cc" in results:
        final_outputs["poh_b2b_cc_final"] = pivot_poh(results["poh_b2b_cc"])

    poh_fsbd_tiktok_frames = []

    if "poh_fsbd" in results:
        poh_fsbd_tiktok_frames.append(results["poh_fsbd"])

    if "poh_tiktok" in results:
        poh_fsbd_tiktok_frames.append(results["poh_tiktok"])

    if poh_fsbd_tiktok_frames:
        results["poh_fsbd_tiktok"] = pd.concat(poh_fsbd_tiktok_frames, ignore_index=True)
        final_outputs["poh_fsbd_tiktok_final"] = pivot_poh(results["poh_fsbd_tiktok"])

    if "no_success_rate_shopee_laz_tt_bd" in results:
        final_outputs["no_success_rate_shopee_laz_tt_bd_final"] = pivot_sr_rts(
            results["no_success_rate_shopee_laz_tt_bd"]
        )

    if "no_rsvn_completed_b2b_cc" in results:
        final_outputs["no_rsvn_completed_b2b_cc_final"] = pivot_rsvn_completed(
            results["no_rsvn_completed_b2b_cc"]
        )

    if "no_attempt_rate_key_shipper" in results:
        final_outputs["no_attempt_rate_key_shipper_final"] = pivot_n0_attempt_rate(
            results["no_attempt_rate_key_shipper"]
        )
    if "assign_inaccuracy" in results:
        final_outputs["assign_inaccuracy_user_final"] = pivot_assignment_inaccuracy_user(
            results["assign_inaccuracy"]
        )
        final_outputs["assign_inaccuracy_hub_final"] = pivot_assignment_inaccuracy_hub(
            results["assign_inaccuracy"]
        )

    if "assign_streamline" in results:
        final_outputs["assign_streamline_final"] = pivot_assignment_streamline(
            results["assign_streamline"]
        )

    if "four_w_productivity" in results:
        final_outputs["four_w_productivity_final"] = pivot_4w_productivity(
            results["four_w_productivity"]
        )

    if "lnd" in results:
        final_outputs["lnd_final"] = select_lnd(results["lnd"])

    if "pst_itv_b2b_cc" in results:
        final_outputs["pst_itv_b2b_cc_final"] = select_itv(results["pst_itv_b2b_cc"])

    if "pst_itv_fsbd" in results:
        final_outputs["pst_itv_fsbd_final"] = select_itv(results["pst_itv_fsbd"])

    if "popa_validity_lazada" in results:
        final_outputs["popa_validity_lazada_final"] = pivot_popa_validity(
            results["popa_validity_lazada"]
        )

    if "popa_validity_aggregator" in results:
        final_outputs["popa_validity_aggregator_final"] = pivot_popa_validity(
            results["popa_validity_aggregator"]
        )

    if "popa_validity_fsbd_lazada" in results:
        final_outputs["popa_validity_fsbd_lazada_final"] = pivot_popa_validity(
            results["popa_validity_fsbd_lazada"]
        )
    if "rot" in results:
        final_outputs["rot_final"] = pivot_rot(results["rot"])

    print("\nSummary final output shapes:")
    for key, df in final_outputs.items():
        print(f"- {key}: {df.shape}")

    print("\n[WRITE] Dump final outputs to Google Sheet...")

    if "poh_fsbd_tiktok_final" in final_outputs:
        write_sheet(
            GSHEET["tracker"]["sheet_id"],
            GSHEET["tracker"]["tabs"]["raw_data_otif"],
            df=final_outputs["poh_fsbd_tiktok_final"],
            start_cell="C4",
            include_header=False,
        )

    if "poh_b2b_cc_final" in final_outputs:
        write_sheet(
            GSHEET["tracker"]["sheet_id"],
            GSHEET["tracker"]["tabs"]["raw_data_otif"],
            df=final_outputs["poh_b2b_cc_final"],
            start_cell="Q4",
            include_header=False,
        )

    if "no_success_rate_shopee_laz_tt_bd_final" in final_outputs:
        write_sheet(
            GSHEET["tracker"]["sheet_id"],
            GSHEET["tracker"]["tabs"]["raw_data_otif"],
            df=final_outputs["no_success_rate_shopee_laz_tt_bd_final"],
            start_cell="AC4",
            include_header=False,
        )

    if "no_rsvn_completed_b2b_cc_final" in final_outputs:
        write_sheet(
            GSHEET["tracker"]["sheet_id"],
            GSHEET["tracker"]["tabs"]["raw_data_otif"],
            df=final_outputs["no_rsvn_completed_b2b_cc_final"],
            start_cell="AL4",
            include_header=False,
        )

    if "no_attempt_rate_key_shipper_final" in final_outputs:
        write_sheet(
            GSHEET["tracker"]["sheet_id"],
            GSHEET["tracker"]["tabs"]["raw_data_otif"],
            df=final_outputs["no_attempt_rate_key_shipper_final"],
            start_cell="AT4",
            include_header=False,
        )

    if "pst_itv_b2b_cc_final" in final_outputs:
        write_sheet(
            GSHEET["tracker"]["sheet_id"],
            GSHEET["tracker"]["tabs"]["raw_data_otif"],
            df=final_outputs["pst_itv_b2b_cc_final"],
            start_cell="BB4",
            include_header=False,
        )

    if "pst_itv_fsbd_final" in final_outputs:
        write_sheet(
            GSHEET["tracker"]["sheet_id"],
            GSHEET["tracker"]["tabs"]["raw_data_otif"],
            df=final_outputs["pst_itv_fsbd_final"],
            start_cell="BJ4",
            include_header=False,
        )

    if "rot_final" in final_outputs:
        write_sheet(
            GSHEET["tracker"]["sheet_id"],
            GSHEET["tracker"]["tabs"]["raw_data_otif"],
            df=final_outputs["rot_final"],
            start_cell="BR4",
            include_header=False,
        )

    print("\n=== FM DAY 2 DONE ===")
    return {
        "raw": results,
        "final": final_outputs,
    }


if __name__ == "__main__":
    run()
