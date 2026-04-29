# ============================================================
# settings.py — Semua konfigurasi pipeline ada di sini
# Kamu cukup update file ini aja, ga perlu utak-atik file lain
# ============================================================

# ── Google Service Account ───────────────────────────────────
# Letakkan file JSON service account kamu di root project
# lalu isi nama file-nya di sini
SERVICE_ACCOUNT_FILE = "service_account.json"

# ── Google Sheets Links ──────────────────────────────────────
GSHEET = {
    # Tracker utama (tempat dump semua data performance)
    "tracker": {
        "url": "https://docs.google.com/spreadsheets/d/1URg6lx6L8jNqxfOL0-k3VSkFECN2hnXOOwCD7OnlvJo/edit?gid=0#gid=0",
        "sheet_id": "1URg6lx6L8jNqxfOL0-k3VSkFECN2hnXOOwCD7OnlvJo",  # ambil dari URL
        "tabs": {
            "raw_data_otif":  "Raw Data [OTIF]",
            "raw_data_inter_cost": "Raw Data [Integrity & Cost]",
            "raw_data_cost": "Raw Data [Cost]",
            "raw_data_assign": "Raw Data [Assignment & Korlap]",
            "staff_list": "Staff List",
            "recipients":"Copy of recipients",
            "master_tracker_by_hub": "Master Tracker by Hub",
        },
        # Range yang di-clear saat Day 1 (sesuaikan)
        "clear_ranges": {
            "raw_data_otif":  ["C4:J","Q4:X","AC4:AH","AL4:AO","AT4:AW","BB4:BE","BJ4:BM","BR4:BU"],
            "raw_data_inter_cost": ["A4:D","I4:N","R4:W"],
            "raw_data_cost": ["B3:T","V3:AF"],
            "raw_data_assign": ["A4:E","G4:K","M4:R","V4:Y","AE4:AF"]
        },
    },
    
    # Gsheet sanggahan
    "sanggahan": {
    "url": "https://docs.google.com/spreadsheets/d/1A7khbGVLlRyOlxfiRSB95LL6Os9J2SyTVpBpLsV-06w/edit?gid=704586042#gid=704586042",
    "sheet_id": "1A7khbGVLlRyOlxfiRSB95LL6Os9J2SyTVpBpLsV-06w",
    "tabs": {
        "pu_to_poh_msh_keyshipper": "PU to PoH MSH Keyshipper",
        "pu_to_poh_msh_b2b_all_b2c_cold": "PU to PoH MSH B2B All & B2C Cold",
        "no_success_rate_rts_shopee_laz_other": "N0 Success Rate RTS Shopee, Laz, Other",
        "no_rsvn_completed_b2b_all_b2c_cold": "N0 RSVN Completed B2B All & B2C Cold",
        "no_attempt_rate_keyshipper": "N0 Attempt Rate Keyshipper",
        "pst_itv_keyshipper": "PST ITV Keyshipper",
        "pst_itv_b2b_all_b2c_cold": "PST ITV B2B All & B2C Cold",
        "rot_b2b_all_b2c_cold": "RoT B2B All & B2C Cold",
        "popa_validity_lazada": "POPA Validity Lazada",
        "popa_validity_aggregator": "POPA Validity Aggregator",
        "popa_validity_fsbd_lazada": "POPA Validity FSBD Lazada",
        "lnd_rate_b2b_all_b2c_cold": "LnD Rate B2B All & B2C Cold",
        "lnd_rate": "LnD Rate",
        "4w_productivity": "4W Productivity",
        "assignment_inaccuracy": "Assignment Inaccuracy",
        "assignment_stream": "Assignment Stream",
        "eki_no_hit": "EKI no hit",
        "staff_list": "Staff List"
    },

    # isi range sendiri nanti
    "clear_ranges": {
        "pu_to_poh_msh_keyshipper": ["A3:H"],
        "pu_to_poh_msh_b2b_all_b2c_cold": ["A3:H"],
        "no_success_rate_rts_shopee_laz_other": ["A3:F"],
        "no_rsvn_completed_b2b_all_b2c_cold": ["A3:D"],
        "no_attempt_rate_keyshipper": ["A3:D"],
        "pst_itv_keyshipper": ["A3:D"],
        "pst_itv_b2b_all_b2c_cold":["A3:D"],
        "rot_b2b_all_b2c_cold": ["A3:D"],
        "popa_validity_lazada": ["A3:F"],
        "popa_validity_aggregator": ["A3:F"],
        "popa_validity_fsbd_lazada": ["A3:F"],
        "lnd_rate_b2b_all_b2c_cold": ["A3:D"],
        "lnd_rate": ["A3:D"],
        "4w_productivity": ["A3:I"],
        "assignment_inaccuracy": ["A3:E"],
        "assignment_stream": ["A3:F"],
        "eki_no_hit": ["A3:B"],
        "staff_list": ["A3:F"]
    }
},

 # Gsheet PNS - sumber list shipper (JANGAN diedit, read only)
    "pns": {
        "url": "https://docs.google.com/spreadsheets/d/15ndhmW4gtQ14uMwMOl33IZ1iS67qQTFEaFhWr-UF7Ns/edit?gid=218596977#gid=218596977",
        "sheet_id": "15ndhmW4gtQ14uMwMOl33IZ1iS67qQTFEaFhWr-UF7Ns",
        "tabs": {
            "compile": "For KPI",
        },
        # Kolom yang diambil dari PNS (sesuaikan)
        "columns": {
            "global_id": "Shipper ID",
            "category": "Type",
        },
    },

    # Gsheet Key Shipper milik BI , copy dari PNS
    "key_shipper": {
        "url": "https://docs.google.com/spreadsheets/d/1Gk_pMm40hHs1jXGTtApLMWXD00HiiRchI2MO-q1HUPQ/edit?gid=1784764051#gid=1784764051",
        "sheet_id": "1Gk_pMm40hHs1jXGTtApLMWXD00HiiRchI2MO-q1HUPQ",
        "tabs": {
            "main": "check",
        },
        # Range yang di-clear sebelum update Key Shipper
        "clear_range": "A2:B",
        # Start cell untuk tulis data
        "start_cell": "A2",
    },

    # Gsheet DWS dari tim Sort
    "param_metabase": {
        "url": "https://docs.google.com/spreadsheets/d/1rPlBaf-iB3AGC7gpkUxMnhqAfoKzMiw2g8jHIFNspKU/edit?gid=0#gid=0",
        "sheet_id": "1rPlBaf-iB3AGC7gpkUxMnhqAfoKzMiw2g8jHIFNspKU",
        "tabs": {
            "param_assignment": "Assignment",
            "param_poh": "POH",
            "param_poh_type_shipper": "POH per Shipper Type",
            "param_cutoff": "Cutoff",
            "param_target": "Target",
            "param_whitelist_hub_itv": "Whitelist Hub ITV",
            "param_exclude_address": "Exclude Address",
            "param_saleschannel_rsvn": "Saleschannel RSVN",
            "param_list_mp": "List MP",
            "param_driver_type": "Driver Type"
}
    },

    # Gsheet CPP dari tim PSP
    "cpp": {
        "url": "https://docs.google.com/spreadsheets/d/1J5QDngNrk1sRGblcGDq3PYzJgF8V5Uv8nwWpC32F4fM/edit?gid=361943273#gid=361943273",
        "sheet_id": "1J5QDngNrk1sRGblcGDq3PYzJgF8V5Uv8nwWpC32F4fM",
        "tabs": {
            "main": "USE THIS", # sesuaikan nama tab
        }
    },

     # Gsheet 2w dari tim PSP
    "2w": {
        "url": "https://docs.google.com/spreadsheets/d/1UpeMQ_QFiq6yhG4z0WAA2N8e2mFGoKXEL7Qn9Rz3dRs/edit?gid=190084916#gid=190084916",
        "sheet_id": "1UpeMQ_QFiq6yhG4z0WAA2N8e2mFGoKXEL7Qn9Rz3dRs",
        "tabs": {
            "main": "USE THIS", # sesuaikan nama tab
        }
    },

     # Gsheet eki dari tim PSP
    "eki": {
        "url": "https://docs.google.com/spreadsheets/d/1qPeQdKyMl9owKx8H4qLDXHKuhU21G0am2T7qPK5Vq0o/edit?gid=0#gid=0",
        "sheet_id": "1qPeQdKyMl9owKx8H4qLDXHKuhU21G0am2T7qPK5Vq0o",
        "tabs": {
            "main": "USE THIS", # sesuaikan nama tab
        }
    },

    # Gsheet kehadiran dari tim PSP
    "kehadiran": {
        "url": "https://docs.google.com/spreadsheets/d/1psfLb-iEEJGzHtsw2nUfCecUrTA7pnQz_e_pnEVEItQ/edit?gid=0#gid=0",
        "sheet_id": "1psfLb-iEEJGzHtsw2nUfCecUrTA7pnQz_e_pnEVEItQ",
        "tabs": {
            "main": "USE THIS", # sesuaikan nama tab
        }
    },

    # Gsheet Converter (data ke rupiah)
    "converter": {
        "url": "https://docs.google.com/spreadsheets/d/1zrmueBzc7QTOXkQ1rFgX6RnDclqFGlBmAcIPthc4t0c/edit?gid=1216663898#gid=1216663898",
        "sheet_id": "1zrmueBzc7QTOXkQ1rFgX6RnDclqFGlBmAcIPthc4t0c",
        "tabs": {
            "master_tracker_by_hub": "Master Tracker by Hub",      # sesuaikan nama tab
            "staff_list":   "Staff List",  # sesuaikan nama tab
        }
    },

    # Gsheet config — tempat kamu simpen Metabase token
    "config": {
        "sheet_id": "1RJK6GFPVrourpdF91GQ1DWuxBBn2a9_SndoyraXckZ4",
        "tabs": {
            "main": "App Password & API Keys",  # nama tab tempat token disimpen
        },
        "token_cell": "B2",  # cell tempat token Metabase
    },
}


# ── Metabase ─────────────────────────────────────────────────
METABASE_CONFIG = {
    "fm": {
        "poh_b2b_cc": {
            "url": "https://metabase.ninjavan.co/api/card/122262/query/json",
            "report_type": "fm",
            "common_params_template": [
                # ===== BASIC =====
                {"id": "c5ac89b7-5d66-5062-c5e6-0f40c5fcf571", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "a6d89202-390d-4ad4-c6b3-c932050f905a", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "23beaf4a-c3c8-d8a9-ce5f-2a7faa597c93", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},

                # ===== FLAG =====
                {"id": "9772d017-4fd1-4cc9-91c5-d791decef1ad", "type": "number/=", "value": [0], "target": ["variable", ["template-tag", "is_mitra_poh"]]},
                {"id": "ce341566-e95e-4014-8c29-460b4aad24bd", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},

                # ===== SHIPPER =====
                {"id": "bf15106e-d476-4d2e-914d-d9f1795b4423", "type": "string/=", "value": "b2b_cc", "target": ["dimension", ["template-tag", "shipper_id"]]},

                # ===== POH PARAMS (B2BR COLUMN) =====
                {"id": "6a8edb0e-155b-468e-8e48-3c1934fbf570", "type": "number/=", "value": "PU_Cutoff_1_Start", "target": ["variable", ["template-tag", "PU_Cutoff_1_Start"]]},
                {"id": "d1de1b96-d336-b5d7-96bf-3194b7dd4f4b", "type": "number/=", "value": "PU_Cutoff_2_Start", "target": ["variable", ["template-tag", "PU_Cutoff_2_Start"]]},
                {"id": "e37fd94d-1d16-5c88-fdcb-7dbec6ad908a", "type": "number/=", "value": "PU_Cutoff_3_Start", "target": ["variable", ["template-tag", "PU_Cutoff_3_Start"]]},
                {"id": "152acebb-d2a6-411d-8d75-5bccaed88e6c", "type": "number/=", "value": "PU_Cutoff_4_Start", "target": ["variable", ["template-tag", "PU_Cutoff_4_Start"]]},

                {"id": "63c0eed1-62dc-0e1b-cbdc-d74270411b50", "type": "number/=", "value": "PU_Cutoff_1_End", "target": ["variable", ["template-tag", "PU_Cutoff_1_End"]]},
                {"id": "66476a89-931b-0464-e49f-e9fa13238098", "type": "number/=", "value": "PU_Cutoff_2_End", "target": ["variable", ["template-tag", "PU_Cutoff_2_End"]]},
                {"id": "126a4d3d-6e4c-4c97-a5ed-4bc5a0e14a2d", "type": "number/=", "value": "PU_Cutoff_3_End", "target": ["variable", ["template-tag", "PU_Cutoff_3_End"]]},
                {"id": "33f0962d-b77f-4146-9432-b88ea99dc5ec", "type": "number/=", "value": "PU_Cutoff_4_End", "target": ["variable", ["template-tag", "PU_Cutoff_4_End"]]},

                {"id": "e5d83ada-c62e-2a87-c313-6cca7891b8d4", "type": "number/=", "value": "HO_Cutoff_1", "target": ["variable", ["template-tag", "HO_Cutoff_1"]]},
                {"id": "886f5945-c6c2-e3aa-71da-54b5ff821ac1", "type": "number/=", "value": "HO_Cutoff_2", "target": ["variable", ["template-tag", "HO_Cutoff_2"]]},
                {"id": "dc23bd24-d703-4ef5-4f8c-18d729f6762e", "type": "number/=", "value": "HO_Cutoff_3", "target": ["variable", ["template-tag", "HO_Cutoff_3"]]},
                {"id": "e4548f50-a133-4753-8b3d-14695654c02d", "type": "number/=", "value": "HO_Cutoff_4", "target": ["variable", ["template-tag", "HO_Cutoff_4"]]},

                {"id": "8a339727-f523-c295-8f4d-d0952249fb1b", "type": "number/=", "value": "Grace_Period_1", "target": ["variable", ["template-tag", "Grace_Period_1"]]},
                {"id": "61cf5e4a-76d0-904a-4646-5a31bb310492", "type": "number/=", "value": "Grace_Period_2", "target": ["variable", ["template-tag", "Grace_Period_2"]]},
                {"id": "8daed83d-f49b-bbe3-7ff6-9b1dbf3119a8", "type": "number/=", "value": "Grace_Period_3", "target": ["variable", ["template-tag", "Grace_Period_3"]]},
                {"id": "6ccd2c1c-98bd-4474-a306-fb1cd628eedd", "type": "number/=", "value": "Grace_Period_4", "target": ["variable", ["template-tag", "Grace_Period_4"]]},

                {"id": "9e5f5b73-61b4-4a12-bc21-9c0b6fae190b", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "prior_flag"]]},
            ],
        },

        "poh_fsbd": {
            "url": "https://metabase.ninjavan.co/api/card/122262/query/json",
            "report_type": "fm",
            "common_params_template": [
                # ===== BASIC ====
                {"id": "c5ac89b7-5d66-5062-c5e6-0f40c5fcf571", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "a6d89202-390d-4ad4-c6b3-c932050f905a", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "23beaf4a-c3c8-d8a9-ce5f-2a7faa597c93", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},

                # ===== FLAG =====
                {"id": "9772d017-4fd1-4cc9-91c5-d791decef1ad", "type": "number/=", "value": [0], "target": ["variable", ["template-tag", "is_mitra_poh"]]},
                {"id": "ce341566-e95e-4014-8c29-460b4aad24bd", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},

                # ===== SHIPPER =====
                {"id": "bf15106e-d476-4d2e-914d-d9f1795b4423", "type": "string/=", "value": "fsbd", "target": ["dimension", ["template-tag", "shipper_id"]]},

                # ===== POH PARAMS (FSBD COLUMN) =====
                {"id": "6a8edb0e-155b-468e-8e48-3c1934fbf570", "type": "number/=", "value": "PU_Cutoff_1_Start", "target": ["variable", ["template-tag", "PU_Cutoff_1_Start"]]},
                {"id": "d1de1b96-d336-b5d7-96bf-3194b7dd4f4b", "type": "number/=", "value": "PU_Cutoff_2_Start", "target": ["variable", ["template-tag", "PU_Cutoff_2_Start"]]},
                {"id": "e37fd94d-1d16-5c88-fdcb-7dbec6ad908a", "type": "number/=", "value": "PU_Cutoff_3_Start", "target": ["variable", ["template-tag", "PU_Cutoff_3_Start"]]},
                {"id": "152acebb-d2a6-411d-8d75-5bccaed88e6c", "type": "number/=", "value": "PU_Cutoff_4_Start", "target": ["variable", ["template-tag", "PU_Cutoff_4_Start"]]},

                {"id": "63c0eed1-62dc-0e1b-cbdc-d74270411b50", "type": "number/=", "value": "PU_Cutoff_1_End", "target": ["variable", ["template-tag", "PU_Cutoff_1_End"]]},
                {"id": "66476a89-931b-0464-e49f-e9fa13238098", "type": "number/=", "value": "PU_Cutoff_2_End", "target": ["variable", ["template-tag", "PU_Cutoff_2_End"]]},
                {"id": "126a4d3d-6e4c-4c97-a5ed-4bc5a0e14a2d", "type": "number/=", "value": "PU_Cutoff_3_End", "target": ["variable", ["template-tag", "PU_Cutoff_3_End"]]},
                {"id": "33f0962d-b77f-4146-9432-b88ea99dc5ec", "type": "number/=", "value": "PU_Cutoff_4_End", "target": ["variable", ["template-tag", "PU_Cutoff_4_End"]]},

                {"id": "e5d83ada-c62e-2a87-c313-6cca7891b8d4", "type": "number/=", "value": "HO_Cutoff_1", "target": ["variable", ["template-tag", "HO_Cutoff_1"]]},
                {"id": "886f5945-c6c2-e3aa-71da-54b5ff821ac1", "type": "number/=", "value": "HO_Cutoff_2", "target": ["variable", ["template-tag", "HO_Cutoff_2"]]},
                {"id": "dc23bd24-d703-4ef5-4f8c-18d729f6762e", "type": "number/=", "value": "HO_Cutoff_3", "target": ["variable", ["template-tag", "HO_Cutoff_3"]]},
                {"id": "e4548f50-a133-4753-8b3d-14695654c02d", "type": "number/=", "value": "HO_Cutoff_4", "target": ["variable", ["template-tag", "HO_Cutoff_4"]]},

                {"id": "8a339727-f523-c295-8f4d-d0952249fb1b", "type": "number/=", "value": "Grace_Period_1", "target": ["variable", ["template-tag", "Grace_Period_1"]]},
                {"id": "61cf5e4a-76d0-904a-4646-5a31bb310492", "type": "number/=", "value": "Grace_Period_2", "target": ["variable", ["template-tag", "Grace_Period_2"]]},
                {"id": "8daed83d-f49b-bbe3-7ff6-9b1dbf3119a8", "type": "number/=", "value": "Grace_Period_3", "target": ["variable", ["template-tag", "Grace_Period_3"]]},
                {"id": "6ccd2c1c-98bd-4474-a306-fb1cd628eedd", "type": "number/=", "value": "Grace_Period_4", "target": ["variable", ["template-tag", "Grace_Period_4"]]},

                {"id": "9e5f5b73-61b4-4a12-bc21-9c0b6fae190b", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "prior_flag"]]},
            ],
        },

        "poh_tiktok": {
            "url": "https://metabase.ninjavan.co/api/card/122262/query/json",
            "report_type": "fm",
            "common_params_template": [
                # ===== BASIC =====
                {"id": "c5ac89b7-5d66-5062-c5e6-0f40c5fcf571", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "a6d89202-390d-4ad4-c6b3-c932050f905a", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "23beaf4a-c3c8-d8a9-ce5f-2a7faa597c93", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},

                # ===== FLAG =====
                {"id": "9772d017-4fd1-4cc9-91c5-d791decef1ad", "type": "number/=", "value": [0], "target": ["variable", ["template-tag", "is_mitra_poh"]]},
                {"id": "ce341566-e95e-4014-8c29-460b4aad24bd", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},

                # ===== PARENT ID COALESCE =====
                {"id": "83e73a9d-1c50-4695-9d92-8208c61b2c35", "type": "string/=", "value": ["7474545"], "target": ["dimension", ["template-tag", "parent_id_coalesce"]]},

                # ===== POH PARAMS (Tiktok COLUMN) =====
                {"id": "6a8edb0e-155b-468e-8e48-3c1934fbf570", "type": "number/=", "value": "PU_Cutoff_1_Start", "target": ["variable", ["template-tag", "PU_Cutoff_1_Start"]]},
                {"id": "d1de1b96-d336-b5d7-96bf-3194b7dd4f4b", "type": "number/=", "value": "PU_Cutoff_2_Start", "target": ["variable", ["template-tag", "PU_Cutoff_2_Start"]]},
                {"id": "e37fd94d-1d16-5c88-fdcb-7dbec6ad908a", "type": "number/=", "value": "PU_Cutoff_3_Start", "target": ["variable", ["template-tag", "PU_Cutoff_3_Start"]]},
                {"id": "152acebb-d2a6-411d-8d75-5bccaed88e6c", "type": "number/=", "value": "PU_Cutoff_4_Start", "target": ["variable", ["template-tag", "PU_Cutoff_4_Start"]]},

                {"id": "63c0eed1-62dc-0e1b-cbdc-d74270411b50", "type": "number/=", "value": "PU_Cutoff_1_End", "target": ["variable", ["template-tag", "PU_Cutoff_1_End"]]},
                {"id": "66476a89-931b-0464-e49f-e9fa13238098", "type": "number/=", "value": "PU_Cutoff_2_End", "target": ["variable", ["template-tag", "PU_Cutoff_2_End"]]},
                {"id": "126a4d3d-6e4c-4c97-a5ed-4bc5a0e14a2d", "type": "number/=", "value": "PU_Cutoff_3_End", "target": ["variable", ["template-tag", "PU_Cutoff_3_End"]]},
                {"id": "33f0962d-b77f-4146-9432-b88ea99dc5ec", "type": "number/=", "value": "PU_Cutoff_4_End", "target": ["variable", ["template-tag", "PU_Cutoff_4_End"]]},

                {"id": "e5d83ada-c62e-2a87-c313-6cca7891b8d4", "type": "number/=", "value": "HO_Cutoff_1", "target": ["variable", ["template-tag", "HO_Cutoff_1"]]},
                {"id": "886f5945-c6c2-e3aa-71da-54b5ff821ac1", "type": "number/=", "value": "HO_Cutoff_2", "target": ["variable", ["template-tag", "HO_Cutoff_2"]]},
                {"id": "dc23bd24-d703-4ef5-4f8c-18d729f6762e", "type": "number/=", "value": "HO_Cutoff_3", "target": ["variable", ["template-tag", "HO_Cutoff_3"]]},
                {"id": "e4548f50-a133-4753-8b3d-14695654c02d", "type": "number/=", "value": "HO_Cutoff_4", "target": ["variable", ["template-tag", "HO_Cutoff_4"]]},

                {"id": "8a339727-f523-c295-8f4d-d0952249fb1b", "type": "number/=", "value": "Grace_Period_1", "target": ["variable", ["template-tag", "Grace_Period_1"]]},
                {"id": "61cf5e4a-76d0-904a-4646-5a31bb310492", "type": "number/=", "value": "Grace_Period_2", "target": ["variable", ["template-tag", "Grace_Period_2"]]},
                {"id": "8daed83d-f49b-bbe3-7ff6-9b1dbf3119a8", "type": "number/=", "value": "Grace_Period_3", "target": ["variable", ["template-tag", "Grace_Period_3"]]},
                {"id": "6ccd2c1c-98bd-4474-a306-fb1cd628eedd", "type": "number/=", "value": "Grace_Period_4", "target": ["variable", ["template-tag", "Grace_Period_4"]]},

                {"id": "9e5f5b73-61b4-4a12-bc21-9c0b6fae190b", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "prior_flag"]]},
            ],
        },
      
        "no_success_rate_shopee_laz_tt_bd": {
            "url": "https://metabase.ninjavan.co/api/card/122265/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "fc584c65-7263-7376-6fb1-493a5d5642b7", "type": "date/single", "value": "start_date" , "target": ["variable", ["template-tag", "start_date"]]},
                {"id": "bc4a93b1-7398-38d2-ca2b-ff575a7e7a7d", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "end_date"]]},
                {"id": "2a99966a-024c-ce38-33c0-9e4d4b062bd5", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "7575936f-5fb5-4fd0-b926-ed0dc60ec15a", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "8ea5d996-fdc4-6822-b89f-9f37eadd275c", "type": "string/=", "value": "driver_list", "target": ["dimension", ["template-tag", "courier_type"]]},
                {"id": "c142f377-ebaa-4f51-a4a8-655ce6553377", "type": "string/=", "value": "bd_shipper", "target": ["dimension", ["template-tag", "shipper_id"]]},
                {"id": "4998d505-7345-4e03-adc3-bdc5544bdfa8", "type": "string/=", "value": ["7474545", "216977", "341107"], "target": ["dimension", ["template-tag", "parent_id_coalesce"]]}
            ],
        },

        "no_rsvn_completed_b2b_cc": {
            "url": "https://metabase.ninjavan.co/api/card/122256/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "190fb3a4-e6cb-4b4e-a78b-f4acb7cc5448", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "26473b49-9801-4240-ade1-6c07b7851c2a", "type": "date/single", "value": "start_end", "target": ["variable", ["template-tag", "start_date"]]},
                {"id": "8d72da7f-6a48-4384-a283-a1c81db37e2d", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "end_date"]]},
                {"id": "cd9e0dbe-b027-4a2a-bb92-bf8175c59aa1", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "f1fca7d5-bddb-42ce-9771-1f17b2c6a1ec", "type": "string/=", "value": "driver_list", "target": ["dimension", ["template-tag", "route_driver_type"]]},
                {"id": "f72285e9-4c7f-4b94-9b22-9cf8c929946f", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "nv_not_liable"]]},
                {"id": "ecfc3da2-aca6-4303-bb42-aa3f9a21810d", "type": "string/contains", "value": ["B2BR"], "target": ["dimension", ["template-tag", "pickup_tags"]], "options": {"case-sensitive": False}},
                {"id": "6980e48f-126e-48d9-a0d3-da79bbd63751", "type": "number/=", "value": "b2b_cc", "target": ["dimension", ["template-tag", "shipper_id"]]}
                # {"id": "52e3d080-5c98-4416-aa1f-dc590efa3d3c", "type": "string/=", "value": key_shipper_list, "target": ["dimension", ["template-tag", "sf_parent_acc_id_coalesce"]]},
                # {"id": "e6bb5201-d1b8-46aa-9b98-e2af5fe6578d", "type": "string/=", "value": ["Restock"], "target": ["dimension", ["template-tag", "sf_nv_product_line"]]},
            ]
        },

        "no_attempt_rate_key_shipper": {
            "url": "https://metabase.ninjavan.co/api/card/122256/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "190fb3a4-e6cb-4b4e-a78b-f4acb7cc5448", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "26473b49-9801-4240-ade1-6c07b7851c2a", "type": "date/single", "value": "start_end", "target": ["variable", ["template-tag", "start_date"]]},
                {"id": "8d72da7f-6a48-4384-a283-a1c81db37e2d", "type": "date/single", "value": "end_end", "target": ["variable", ["template-tag", "end_date"]]},
                {"id": "cd9e0dbe-b027-4a2a-bb92-bf8175c59aa1", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "f1fca7d5-bddb-42ce-9771-1f17b2c6a1ec", "type": "string/=", "value": "driver_type", "target": ["dimension", ["template-tag", "route_driver_type"]]},
                {"id": "6980e48f-126e-48d9-a0d3-da79bbd63751", "type": "number/=", "value": "fsbd", "target":["dimension", ["template-tag", "shipper_id"]]}
                # {"id": "452ee39f-7548-48f9-88aa-5348c9addd86", "type": "number/=", "value": parent_id_list, "target":["dimension",["template-tag","parent_id_coalesce"]]}
            ],
        },

        "pst_itv": {
            "url": "https://metabase.ninjavan.co/api/card/122382/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "73b82b17-f104-4e8e-97a5-893bead6e23d", "type": "number/=", "value": "cutoff1", "target": ["variable", ["template-tag", "cutoff1"]]},
                {"id": "6e097897-9131-4290-9e72-df0a88810fb5", "type": "number/=", "value": "base_cutoff", "target": ["variable", ["template-tag", "base_cutoff"]]},
                {"id": "3b1e2bba-7910-467e-b990-ebbeac9104ef", "type": "number/=", "value": "cutoff2", "target": ["variable", ["template-tag", "cutoff2"]]},
                {"id": "667af047-21e0-4308-abf9-8e7e015dc173", "type": "string/=", "value": "hub_whitelist1", "target": ["dimension", ["template-tag", "whitelist_hub1"]]},
                {"id": "933b6ecb-ebdb-43ba-a081-f601e77a7312", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "0ce6735d-ef50-4044-b2ed-46a62573a711", "type": "date/all-options", "value": "period_str", "target": ["dimension", ["template-tag", "pickup_date"]]},
                {"id": "0a1bebfe-b890-4dba-9c02-afe4c5a8c948", "type": "string/=", "value": "hub_whitelist2", "target": ["dimension", ["template-tag", "whitelist_hub2"]]},
                {"id": "63333156-a5a8-4418-9e7f-0a41734f57de", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "prior_flag"]]}
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {"id": "0822034a-6d21-4110-b68d-13ed9987bc95", "type": "string/=", "value": "b2b_cc", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
                "fsbd": [
                    {"id": "0822034a-6d21-4110-b68d-13ed9987bc95", "type": "string/=", "value": "fsbd", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
            },
        },

        "rot": {
            "url": "https://metabase.ninjavan.co/api/card/122256/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "190fb3a4-e6cb-4b4e-a78b-f4acb7cc5448", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "26473b49-9801-4240-ade1-6c07b7851c2a", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "start_date"]]},
                {"id": "8d72da7f-6a48-4384-a283-a1c81db37e2d", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "end_date"]]},
                {"id": "cd9e0dbe-b027-4a2a-bb92-bf8175c59aa1", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "f1fca7d5-bddb-42ce-9771-1f17b2c6a1ec", "type": "string/=", "value": "driver_list", "target": ["dimension", ["template-tag", "route_driver_type"]]},
                {"id": "ecfc3da2-aca6-4303-bb42-aa3f9a21810d", "type": "string/contains", "value": ["B2BR"], "target": ["dimension", ["template-tag", "pickup_tags"]], "options": {"case-sensitive": False}},
                {"id": "6980e48f-126e-48d9-a0d3-da79bbd63751", "type": "number/=", "value": "b2b_cc", "target": ["dimension", ["template-tag", "shipper_id"]]},
                # {"id": "52e3d080-5c98-4416-aa1f-dc590efa3d3c", "type": "string/=", "value": key_shipper_list, "target": ["dimension", ["template-tag", "sf_parent_acc_id_coalesce"]]}
                # {"id": "e6bb5201-d1b8-46aa-9b98-e2af5fe6578d", "type": "string/=", "value": ["Restock"], "target": ["dimension", ["template-tag", "sf_nv_product_line"]]},
            ],
        },

        "lnd": {
            "url": "https://metabase.ninjavan.co/api/card/122271/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "942b232c-31f7-f535-440f-4cce5562023f", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "d0c21291-d053-49f7-9012-0f975163daf8", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "9a452715-48aa-6fb3-e8ff-5a5990b2ab16", "type": "date/single", "value": "start_end", "target": ["variable", ["template-tag", "start"]]},
                {"id": "a5d4bb81-ad4f-cfbd-39c2-ea81f40f5cee", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag","end"]]},
                {"id": "6bdaad0f-d9e2-4f12-b420-f0eddaa31bb9", "type": "string/=", "value": "b2b_cc", "target": ["dimension", ["template-tag", "shipper_id"]]},
            ],
        },

        "popa_validity": {
            "url": "https://metabase.ninjavan.co/api/card/122267/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "353d7399-af47-4a79-ac23-e11d11ebc918", "type": "string/=", "value": "driver_list", "target": ["dimension", ["template-tag", "courier_type"]]},
                {"id": "656b69d2-6530-48a7-80fb-a2565c2b4735", "type": "category", "value": ["Core"], "target": ["variable", ["template-tag", "pickup_by"]]},
                {"id": "11c97a25-3f02-42ad-98e5-166f97a255f0", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "597a35aa-1671-b4fb-23f9-46f06da60b16", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "e7680960-c1c8-477d-8686-0a038fc680a8", "type": "date/all-options", "value": "period_str", "target": ["dimension", ["template-tag", "attempt_date"]]},
                
            ],
            "shipper_params_template": {
                "lazada": [
                    {"id": "1158f7c8-4916-47f7-af7e-4718227cf10c", "type": "string/=", "value": [341107], "target": ["dimension", ["template-tag", "parent_id_coalesce"]]},
                ],
                "aggregator": [
                    {"id": "326bf38c-b686-4319-acef-dbb678227625", "type": "string/=", "value": "aggregator", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
                "fsbd_lazada": [
                    {"id": "326bf38c-b686-4319-acef-dbb678227625", "type": "string/=", "value": "fsbd", "target": ["dimension", ["template-tag", "shipper_id"]]},
                    {"id": "1158f7c8-4916-47f7-af7e-4718227cf10c", "type": "string/=", "value": [341107], "target": ["dimension", ["template-tag", "parent_id_coalesce"]]}
                ],
            },
        },

        "assign_inaccuracy": {
            "url": "https://metabase.ninjavan.co/question/113533/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "207c1942-61d1-488d-8fea-0956e6f1f4fc", "type": "string/=", "value": "driver_list", "target": ["dimension", ["template-tag", "route_driver_type"]]},
                {"id": "81067f90-3579-4135-8c4e-353934cb6d04", "type": "string/=", "value": ["COMPLETED", "Success"], "target": ["dimension", ["template-tag", "status"]]},
                {"id": "7f44a418-7b61-4949-9f27-16bd983ce496", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "start"]]},
                {"id": "d4f96a68-280c-4f69-8b17-c91341d69291", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "end"]]},
                {"id": "87e7422d-4d68-4223-b08f-6adca77cf9cd", "type": "number/=", "value": [60], "target": ["variable", ["template-tag", "target_pdv"]]},
                {"id": "a6d11133-5938-4d78-983d-3da0675c70d6", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "show_rsvn_below_target_only"]]},
                {"id": "90025015-db73-43a6-98b5-ab9e122626d7", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "2b5ddda7-de30-4687-884b-9c338e6e1615", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "4f1cee13-7b68-42ba-ba29-24ebe3082b5b", "type": "number/!=", "value": [1], "target": ["dimension", ["template-tag", "address_id"]]}
            ],
        },

        "assign_streamline": {
            "url": "https://metabase.ninjavan.co/question/99742/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "177476c2-e00a-40d1-b133-a52d21917162", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "start_ready_datetime"]]},
                {"id": "36571bdd-01cb-4c49-b3b0-8423d4111475", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "end_ready_datetime"]]},
                {"id": "b8c4d58d-4c6d-4fba-88d0-a8092a5d438f", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "1113fbec-63bb-4a28-a5e6-c5ed90ec85e5", "type": "string/=", "value": ["Central Java", "East Java", "Greater Jakarta", "West Java"], "target": ["dimension", ["template-tag", "assigned_region"]]},
                {"id": "ffc48f18-04a7-4a4f-93a5-b44724a988d3", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "exclude_courier_type_mitra"]]},
                {"id": "a666970b-4faa-4498-a86b-25dc9fca166c", "type": "category", "value": ["Core"], "target": ["variable", ["template-tag", "pickup_by"]]},
                {"id": "aaf4e5d9-2fda-40b6-b06b-189a8a057cfd", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},

                {"id": "121a1b50-8ac8-4063-9141-c3d5ae848c93", "type": "category", "value": "lt_hour_scheduled_cutoff_1", "target": ["variable", ["template-tag", "lt_hour_scheduled_cutoff_1"]]},
                {"id": "58418b60-66e1-40dd-b3da-a84859b4060a", "type": "category", "value": "lt_hour_scheduled_cutoff_2", "target": ["variable", ["template-tag", "lt_hour_scheduled_cutoff_2"]]},
                {"id": "250780cd-1cbc-4d3a-a474-c6ee4ab76aa2", "type": "category", "value": "lt_hour_scheduled_cutoff_3", "target": ["variable", ["template-tag", "lt_hour_scheduled_cutoff_3"]]},
                {"id": "67c22eb2-7960-483b-8971-960197e6ae2c", "type": "category", "value": "lt_hour_scheduled_cutoff_4", "target": ["variable", ["template-tag", "lt_hour_scheduled_cutoff_4"]]},

                {"id": "65eff729-6929-4f7d-8228-a4be53e73c3b", "type": "category", "value": "lt_hour_after_creation_cutoff_1", "target": ["variable", ["template-tag", "lt_hour_after_creation_cutoff_1"]]},
                {"id": "6465e475-f93e-419f-8299-587ad49affad", "type": "category", "value": "lt_hour_after_creation_cutoff_2", "target": ["variable", ["template-tag", "lt_hour_after_creation_cutoff_2"]]},
                {"id": "91d0d421-a736-497d-97d9-5c2106cda478", "type": "category", "value": "lt_hour_after_creation_cutoff_3", "target": ["variable", ["template-tag", "lt_hour_after_creation_cutoff_3"]]},
                {"id": "1c1c241e-da8d-49c1-a236-54a71050c781", "type": "category", "value": "lt_hour_after_creation_cutoff_4", "target": ["variable", ["template-tag", "lt_hour_after_creation_cutoff_4"]]},

                {"id": "a3c7c85c-3611-44e8-8bf3-a606a707eb0c", "type": "number/=", "value": "start_rsvn_creation_cutoff_1", "target": ["variable", ["template-tag", "start_rsvn_creation_cutoff_1"]]},
                {"id": "74392b19-15c2-4a72-a1d1-21208d46d1b0", "type": "number/=", "value": "start_rsvn_creation_cutoff_2", "target": ["variable", ["template-tag", "start_rsvn_creation_cutoff_2"]]},
                {"id": "530bf042-7530-45b3-8c6e-7c442295991d", "type": "number/=", "value": "start_rsvn_creation_cutoff_3", "target": ["variable", ["template-tag", "start_rsvn_creation_cutoff_3"]]},
                {"id": "1ff0e147-834d-457e-b168-5ed5c7396344", "type": "number/=", "value": "start_rsvn_creation_cutoff_4", "target": ["variable", ["template-tag", "start_rsvn_creation_cutoff_4"]]},

                {"id": "9e054dbc-b16a-4cda-8162-709b0dcd1b53", "type": "number/=", "value": "end_rsvn_creation_cutoff_1", "target": ["variable", ["template-tag", "end_rsvn_creation_cutoff_1"]]},
                {"id": "2e995bac-4d31-4d40-8b6a-f462b33aad75", "type": "number/=", "value": "end_rsvn_creation_cutoff_2", "target": ["variable", ["template-tag", "end_rsvn_creation_cutoff_2"]]},
                {"id": "dfc84362-ba4c-48e1-9719-47e9b6ea6054", "type": "number/=", "value": "end_rsvn_creation_cutoff_3", "target": ["variable", ["template-tag", "end_rsvn_creation_cutoff_3"]]},
                {"id": "2bd27d40-1cfe-4036-91cc-5d7b8051b556", "type": "number/=", "value": "end_rsvn_creation_cutoff_4", "target": ["variable", ["template-tag", "end_rsvn_creation_cutoff_4"]]},

                {"id": "dbf8504d-c2f3-45d5-b978-e0f347847368", "type": "category", "value": "lt_type_cutoff_1", "target": ["variable", ["template-tag", "lt_type_cutoff_1"]]},
                {"id": "55b6e513-416a-4745-8e7c-9297e2eb4a46", "type": "category", "value": "lt_type_cutoff_2", "target": ["variable", ["template-tag", "lt_type_cutoff_2"]]},
                {"id": "0b7dc1a3-cd32-4c70-959b-9f9450e07456", "type": "category", "value": "lt_type_cutoff_3", "target": ["variable", ["template-tag", "lt_type_cutoff_3"]]},
                {"id": "6fa92d2c-f48c-436d-913b-1b380227315f", "type": "category", "value": "lt_type_cutoff_4", "target": ["variable", ["template-tag", "lt_type_cutoff_4"]]},

                {"id": "57535593-3654-4b0c-85a7-f58c33aad2b8", "type": "category", "value": "lt_grace_period_day_cutoff_1", "target": ["variable", ["template-tag", "lt_grace_period_day_cutoff_1"]]},
                {"id": "a0df0bb1-a194-497d-808b-e8cb872aaa12", "type": "category", "value": "lt_grace_period_day_cutoff_2", "target": ["variable", ["template-tag", "lt_grace_period_day_cutoff_2"]]},
                {"id": "9c65579f-6aa3-4166-98fd-232012701551", "type": "category", "value": "lt_grace_period_day_cutoff_3", "target": ["variable", ["template-tag", "lt_grace_period_day_cutoff_3"]]},
                {"id": "19087b6e-634d-4a52-847a-c17c5ab800bd", "type": "category", "value": "lt_grace_period_day_cutoff_4", "target": ["variable", ["template-tag", "lt_grace_period_day_cutoff_4"]]},

                {"id": "c6de76aa-bf15-4b28-897f-801612de63d2", "type": "number/=", "value": [0], "target": ["variable", ["template-tag", "rot_assign_cutoff_hour"]]},
                {"id": "23f6960c-e4a8-440c-b7c2-8463d99c9031", "type": "number/=", "value": [0], "target": ["variable", ["template-tag", "rot_remove_cutoff_hour"]]}
            ]
        },

        "four_w_productivity": {
            "url": "https://metabase.ninjavan.co/question/99900/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "0ddfdd63-4858-404f-9391-4c0a6f3c77ea", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "sph_flag"]]},
                {"id": "eb91b326-11ef-4c9b-8a86-c09184c3c5e7", "type": "number/=", "value": "4w_gj_target", "target": ["variable", ["template-tag", "4w_gj_target"]]},
                {"id": "4fbb553b-55fd-46c2-ae34-ebcb2163e214", "type": "number/=", "value": "4w_wj_target", "target": ["variable", ["template-tag", "4w_wj_target"]]},
                {"id": "6c19c33b-a5e9-48c7-8a1c-b139333e568a", "type": "number/=", "value": "4w_cj_target", "target": ["variable", ["template-tag", "4w_cj_target"]]},
                {"id": "06fa8173-3e61-488e-b149-a2d398a9fa63", "type": "number/=", "value": "4w_ej_target", "target": ["variable", ["template-tag", "4w_ej_target"]]},
                {"id": "f446e2fb-0e69-49ef-b18b-d66cbeb01526", "type": "number/=", "value": "2w_gj_target", "target": ["variable", ["template-tag", "2w_gj_target"]]},
                {"id": "7ec8a31e-1a9f-42e5-9cf2-5e5dec9722cb", "type": "number/=", "value": "2w_wj_target", "target": ["variable", ["template-tag", "2w_wj_target"]]},
                {"id": "d8866130-3fe4-4095-9384-bb6b8ec29a14", "type": "number/=", "value": "2w_cj_target", "target": ["variable", ["template-tag", "2w_cj_target"]]},
                {"id": "1f329f60-9dfe-47eb-92dc-02e3de8860eb", "type": "number/=", "value": "2w_ej_target", "target": ["variable", ["template-tag", "2w_ej_target"]]},
                {"id": "ded95caf-a5b4-42e4-977f-f4dda31b516d", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "e84c7565-cb41-4f04-9b14-0bce69655758", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "253b3b7f-bf13-4e3b-a7c8-7bf40655feaa", "type": "date/all-options", "value": "period_str", "target": ["dimension", ["template-tag", "attempt_date"]]},
                {"id": "07126788-e4f1-4fb6-8f8d-5ba18d51d884", "type": "string/=", "value": ["East Java", "Central Java", "Greater Jakarta", "West Java"], "target": ["dimension", ["template-tag", "hub_region"]]}
            ]
        },
    }
}
# ── Archieved File ─────────────────────────────────────────────────────
ARCHIVE_CONFIG = {
    "tracker": {
        "source_file_id": "10jwwERVKLvdrk7tkmqVXeZHGp3Q1lV_2IjFsc6fXQhQ",
        "target_folder_id": "18BwwadT0kgyPgvdmOg3b7CP29zqrTFB4",
    },
    "sanggahan": {
        "source_file_id": "1q1CkYFiZQKRvfYDjZGOJmqNOndbH3hd7Du_Pq0Wn7AU",
        "target_folder_id": "12d8VANvDb2earFpAJOgQLj4kW1ITZm_U",
    },
    "converter": {
        "source_file_id": "1Sn2HisZcT81duWuWtKpVx_E_8192XeFIwtXrrDoSpGQ",
        "target_folder_id": "1Dx2EJoddhhdSqJs5qkNG8rWB9ydCc1Sl",
    },
}

# ── Pipeline Schedule ─────────────────────────────────────────
# Ini untuk referensi GitHub Actions
# Tanggal yang pipeline jalan tiap bulan
SCHEDULE_DAYS = [1, 2, 6, 10, 14, 15, 16]
