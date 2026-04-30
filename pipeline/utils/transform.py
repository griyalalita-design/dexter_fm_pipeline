# ============================================================
# utils/transform.py — Semua transformasi data pake pandas
# TIDAK ada API calls di sini, murni transformasi aja
# ============================================================

import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta


def get_last_month_range():
    """
    Hitung range bulan lalu.
    Contoh: kalau sekarang April 2026, return (2026-03-01, 2026-03-31, 'Maret')
    """
    today = date.today()
    start_day = (today.replace(day=1) - relativedelta(months=1))
    end_day = today.replace(day=1) - relativedelta(days=1)
    bulan_names = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
        5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
        9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    bulan_name = bulan_names[first_day.month]
    return start_day, end_day, bulan_name


def categorize_shippers(df_pns: pd.DataFrame):
    """
    Bagi shipper dari Key Shipper ke kategori Day 2.

    Returns:
        dict dengan keys: "b2b_cc", "key_shipper", "lazada_shopee"
        masing-masing berisi list Global ID (int).
    """
    required_cols = ["Global ID", "Shipper Service Category"]
    missing_cols = [c for c in required_cols if c not in df_pns.columns]
    if missing_cols:
        raise ValueError(
            f"Kolom wajib tidak ditemukan di key shipper sheet: {missing_cols}. "
            "Pastikan header: 'Global ID' dan 'Shipper Service Category'."
        )

    df = df_pns.copy()
    df["Shipper Service Category"] = df["Shipper Service Category"].astype(str).str.strip()
    df["Global ID"] = pd.to_numeric(df["Global ID"], errors="coerce")
    df = df[df["Global ID"].notna()]
    df["Global ID"] = df["Global ID"].astype(int)

    b2b_cc_categories = ["B2BR", "B2BR Sameday", "LTL Reguler"]
    key_shipper_category = "FS / BD Key Shipper"

    b2b_cc = (
        df[df["Shipper Service Category"].isin(b2b_cc_categories)]["Global ID"]
        .dropna()
        .astype(int)
        .drop_duplicates()
        .tolist()
    )

    key_shipper = (
        df[df["Shipper Service Category"] == key_shipper_category]["Global ID"]
        .dropna()
        .astype(int)
        .drop_duplicates()
        .tolist()
    )


    print(f"Shipper B2B+CC: {len(b2b_cc)}")
    print(f"Key Shipper: {len(key_shipper)}")

    return {
        "b2b_cc": b2b_cc,
        "key_shipper": key_shipper,
    }

# utils/transform.py
import numpy as np
import pandas as pd


def _normalize_status(value: str) -> str:
    if value is None:
        return "unknown"
    value = str(value).strip().lower()
    if value in {"hit", "yes", "y", "1"}:
        return "hit"
    if value in {"not hit", "no", "n", "0", "miss"}:
        return "not_hit"
    return value.replace(" ", "_")



def pivot_assignment_streamline(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    work = df[["rsvn_ready_date_aggr", "final_user_id", "final_assignment_streamline_flag"]].copy()
    return (
        work.groupby(["rsvn_ready_date_aggr", "final_user_id"], as_index=False)
        .agg(
            hit=("final_assignment_streamline_flag", lambda x: (x == 1).sum()),
            not_hit=("final_assignment_streamline_flag", lambda x: (x == 0).sum()),
            grand_total=("final_assignment_streamline_flag", "count"),
        )
    )


def pivot_assignment_inaccuracy_user(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    work = df[["aggr_attempt_date", "final_user_id", "vehicle_type"]].copy()
    return (
        work.groupby(["aggr_attempt_date", "final_user_id"], as_index=False)
        .agg(
            two_wheel=("vehicle_type", lambda x: (x == "2w").sum()),
            four_wheel=("vehicle_type", lambda x: (x == "4w").sum()),
            total_rsvn=("vehicle_type", "count"),
        )
    )


def pivot_assignment_inaccuracy_hub(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    work = df[["aggr_attempt_date", "hub_name", "vehicle_type"]].copy()
    return (
        work.groupby(["aggr_attempt_date", "hub_name"], as_index=False)
        .agg(
            two_wheel=("vehicle_type", lambda x: (x == "2w").sum()),
            four_wheel=("vehicle_type", lambda x: (x == "4w").sum()),
            total_rsvn=("vehicle_type", "count"),
        )
    )


def pivot_n0_attempt_rate(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    work = df[["rsvn_ready_date", "hub_name", "rsvn_n0_attempt_hit", "rsvn_ready"]].copy()
    return (
        work.groupby(["rsvn_ready_date", "hub_name"], as_index=False)
        .agg(
            n0_attempt=("rsvn_n0_attempt_hit", "sum"),
            grand_total=("rsvn_ready", "sum"),
        )
    )


def pivot_rsvn_completed(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    work = df[["rsvn_ready_date", "hub_name", "rsvn_n0_success_hit", "rsvn_ready"]].copy()
    return (
        work.groupby(["rsvn_ready_date", "hub_name"], as_index=False)
        .agg(
            n0_success=("rsvn_n0_success_hit", "sum"),
            grand_total=("rsvn_ready", "sum"),
        )
    )


def pivot_rot(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    work = df[["rsvn_ready_date", "hub_name", "rsvn_ontime", "rsvn_ready"]].copy()
    return (
        work.groupby(["rsvn_ready_date", "hub_name"], as_index=False)
        .agg(
            rsvn_ontime=("rsvn_ontime", "sum"),
            grand_total=("rsvn_ready", "sum"),
        )
    )


def pivot_poh(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    cols = ["aggr", "hub_name", "hit_cutoff1", "hit_cutoff2", "hit_cutoff3", "hit_cutoff4", "total_vol"]
    work = df[cols].copy()
    work["total_hit"] = (
        work[["hit_cutoff1", "hit_cutoff2", "hit_cutoff3", "hit_cutoff4"]]
        .fillna(0)
        .sum(axis=1)
    )
    return (
        work.groupby(["aggr", "hub_name"], as_index=False)
        .agg(
            hit_cutoff1=("hit_cutoff1", "sum"),
            hit_cutoff2=("hit_cutoff2", "sum"),
            hit_cutoff3=("hit_cutoff3", "sum"),
            hit_cutoff4=("hit_cutoff4", "sum"),
            total_hit=("total_hit", "sum"),
            total_vol=("total_vol", "sum"),
        )
    )


def pivot_popa_validity(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    work = df[
        [
            "attempt_date_aggr",
            "hub_region",
            "hub_name",
            "validation_remarks_hit_n1",
            "final_validity_remarks",
            "transaction_id",
        ]
    ].copy()
    out = (
        work.groupby(["attempt_date_aggr", "hub_region", "hub_name"], as_index=False)
        .agg(
            total_hit_n1=("validation_remarks_hit_n1", lambda x: (x == "Hit").sum()),
            total_valid=("final_validity_remarks", lambda x: (x == "Valid").sum()),
            total_invalid=("final_validity_remarks", lambda x: (x == "Invalid").sum()),
            total_validation=("final_validity_remarks", lambda x: x.isin(["Valid", "Invalid"]).sum()),
            total_transactions=("transaction_id", "count"),
        )
    )
    out["hit_n1_valid_rate"] = np.where(
        out["total_transactions"] > 0,
        out["total_hit_n1"] / out["total_transactions"],
        0,
    )
    out["validity_rate"] = np.where(
        out["total_validation"] > 0,
        out["total_valid"] / out["total_validation"],
        0,
    )
    return out[
        [
            "attempt_date_aggr",
            "hub_region",
            "hub_name",
            "total_hit_n1",
            "hit_n1_valid_rate",
            "total_valid",
            "total_invalid",
            "validity_rate",
            "total_transactions",
        ]
    ]


def pivot_sr_rts(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()

    work = df[
        [
            "aggr_route_time",
            "hub_region",
            "hub_name",
            "total_completed_rts_orders",
            "total_attempted_rts_orders",
        ]
    ].copy()
    work["miss_completed_rts_orders"] = (
        work["total_attempted_rts_orders"].fillna(0) - work["total_completed_rts_orders"].fillna(0)
    )
    return (
        work.groupby(["aggr_route_time", "hub_region", "hub_name"], as_index=False)
        .agg(
            total_completed_rts_orders=("total_completed_rts_orders", "sum"),
            miss_completed_rts_orders=("miss_completed_rts_orders", "sum"),
            total_attempted_rts_orders=("total_attempted_rts_orders", "sum"),
        )
    )


def select_lnd(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()
    return df[["aggr", "hub", "total_loss_damage", "total_volume"]].copy()


def select_itv(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df.copy()
    return df[["aggr", "pickup_hub_name", "pickup_hub_region", "pickup_vol", "hit_n0_itv", "n0_itv_rate"]].copy()


def apply_reviewed_sanggahan(tracker_df: pd.DataFrame, sanggahan_df: pd.DataFrame) -> pd.DataFrame:
    """
    Replace tracker metrics with reviewed sanggahan values (same columns).
    TODO: Define primary keys and exact columns to overwrite.
    """
    if tracker_df.empty or sanggahan_df.empty:
        return tracker_df.copy()

    # Placeholder logic: prefer sanggahan rows if matching key exists.
    # Replace with real merge keys and overwrite logic.
    return tracker_df


def check_anomaly(df: pd.DataFrame) -> pd.DataFrame:
    """
    Flag anomaly conditions (DIV/NA/empty performance).
    TODO: Implement real anomaly rules and add a boolean column.
    """
    if df.empty:
        return df.copy()

    result = df.copy()
    result["anomaly_flag"] = False
    return result


def build_performance_summary(tracker_df: pd.DataFrame) -> pd.DataFrame:
    """
    Build a performance summary for reporting/notification.
    TODO: Define summary metrics.
    """
    return tracker_df.head(0).copy()
