import pandas as pd
from utils.gsheet import open_by_key, write_sheet, copy_range
from config.settings import GSHEET


def read_range_as_df(sheet_id, tab_name, range_a1):
    wb = open_by_key(sheet_id)
    values = wb.values_get(f"{tab_name}!{range_a1}").get("values", [])

    if not values:
        return pd.DataFrame()

    header = values[0]
    data = values[1:]

    df = pd.DataFrame(data, columns=header)
    return df


def run():
    print("===== Kita Mulai Run Day 16 =====")

    # 🔥 Read range A6:AQ (header di A6)
    df_master = read_range_as_df(
        GSHEET["tracker"]["sheet_id"],
        GSHEET["tracker"]["tabs"]["master_tracker_by_hub"],
        "A6:AQ"
    )

    print(f"Before filter: {df_master.shape}")
    print("Columns:", df_master.columns.tolist())

    # Kolom F = index 5, G = index 6
    col_f = df_master.columns[5]
    col_g = df_master.columns[6]

    df_filtered = df_master[
        (df_master[col_g].astype(str).str.strip().str.lower() == "eligible") &
        (df_master[col_f].astype(str).str.strip().str.lower() == "jawo")
    ].copy()

    print(f"After filter: {df_filtered.shape}")

    # 🔥 Write tanpa header ke A7
    write_sheet(
        spreadsheet_id=GSHEET["converter"]["sheet_id"],
        sheet_name=GSHEET["converter"]["tabs"]["master_tracker_by_hub"],
        df=df_filtered,
        start_cell="A4",
        include_header=False,
    )

    print("===== Filter + input summary tracker ke converter done =====")

    # Copy staff list tetap pakai copy_range
    copy_range(
        source_sheet_id=GSHEET["tracker"]["sheet_id"],
        source_tab=GSHEET["tracker"]["tabs"]["staff_lis"],
        source_range="A2:H",
        dest_sheet_id=GSHEET["converter"]["sheet_id"],
        dest_tab=GSHEET["converter"]["tabs"]["staff_list"],
        dest_start_cell="A2",
    )

    print("===== Copy staff list ke converter done =====")


if __name__ == "__main__":
    run()
