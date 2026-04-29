# jobs/day15.py
from utils.gsheet import copy_range
from config.settings import GSHEET


def run():
    print("===== Kita Mulai Run Day 15 Review Sanggahan =====")

    # PU to PoH MSH Keyshipper -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["pu_to_poh_msh_keyshipper"],
        source_range="Q3:X",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab=GSHEET["tracker"]["tabs"]["raw_data_otif"],
        dest_start_cell="C4",
    )
    print("===== PU to PoH MSH Keyshipper -> Tracker Done =====")

    # PU to PoH MSH B2B All & B2C Cold -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["pu_to_poh_msh_b2b_all_b2c_cold"],
        source_range="Q3:X",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab=GSHEET["tracker"]["tabs"]["raw_data_otif"],
        dest_start_cell="Q4",
    )
    print("===== PU to PoH MSH B2B All & B2C Cold -> Tracker Done =====")

    # N0 Success Rate RTS Shopee, Laz, Other -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["no_success_rate_rts_shopee_laz_other"],
        source_range="P3:U",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab=GSHEET["tracker"]["tabs"]["raw_data_otif"],
        dest_start_cell="AC4",
    )
    print("===== N0 Success Rate RTS Shopee, Laz, Other -> Tracker Done =====")

    # N0 RSVN Completed B2B All & B2C Cold -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["no_rsvn_completed_b2b_all_b2c_cold"],
        source_range="M3:P,
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab=GSHEET["tracker"]["tabs"]["raw_data_otif"],
        dest_start_cell="AL4",
    )
    print("===== N0 RSVN Completed B2B All & B2C Cold -> Tracker Done =====")

    # N0 Attempt Rate Keyshipper -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["no_attempt_rate_keyshipper"],
        source_range="M3:P",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab=GSHEET["tracker"]["tabs"]["raw_data_otif"],
        dest_start_cell="AT4",
    )
    print("===== N0 Attempt Rate Keyshipper -> Tracker Done =====")

    # PST ITV Keyshipper -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["pst_itv_keyshipper"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== PST ITV Keyshipper -> Tracker Done =====")

    # RoT B2B All & B2C Cold -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["rot_b2b_all_b2c_cold"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== RoT B2B All & B2C Cold -> Tracker Done =====")

    # POPA Validity Lazada -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["popa_validity_lazada"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== POPA Validity Lazada -> Tracker Done =====")

    # POPA Validity Aggregator -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["popa_validity_aggregator"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== POPA Validity Aggregator -> Tracker Done =====")

    # POPA Validity FSBD Lazada -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["popa_validity_fsbd_lazada"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== POPA Validity FSBD Lazada -> Tracker Done =====")

    # LnD Rate B2B All & B2C Cold -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["lnd_rate_b2b_all_b2c_cold"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== LnD Rate B2B All & B2C Cold -> Tracker Done =====")

    # LnD Rate -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["lnd_rate"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== LnD Rate -> Tracker Done =====")

    # 4W Productivity -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["4w_productivity"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== 4W Productivity -> Tracker Done =====")

    # Assignment Inaccuracy -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["assignment_inaccuracy"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== Assignment Inaccuracy -> Tracker Done =====")

    # Assignment Stream -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["assignment_stream"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== Assignment Stream -> Tracker Done =====")

    # EKI no hit -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["eki_no_hit"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== EKI no hit -> Tracker Done =====")

    # Staff List -> Tracker
    copy_range(
        source_sheet_id=GSHEET["sanggahan"]["sheet_id"],
        source_tab=GSHEET["sanggahan"]["tabs"]["staff_list"],
        source_range="TODO_SOURCE_RANGE",
        dest_sheet_id=GSHEET["tracker"]["sheet_id"],
        dest_tab="TODO_DEST_TAB",
        dest_start_cell="TODO_DEST_START_CELL",
    )
    print("===== Staff List -> Tracker Done =====")

    print("===== Day 15 Done =====")


if __name__ == "__main__":
    run()
