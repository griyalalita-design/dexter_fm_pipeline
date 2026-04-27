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
            "recipients":"recipients",
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
        "pu_to_poh_msh_non_keyshipper": "PU to PoH MSH Non Keyshipper",
        "pu_to_poh_msh_b2b_all_b2c_cold": "PU to PoH MSH B2B All & B2C Cold",
        "no_success_rate_rts_shopee_laz_other": "N0 Success Rate RTS Shopee, Laz, Other",
        "no_rsvn_completed_b2b_all_b2c_cold": "N0 RSVN Completed B2B All & B2C Cold",
        "no_attempt_rate_keyshipper": "N0 Attempt Rate Keyshipper",
        "pst_itv_keyshipper": "PST ITV Keyshipper",
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
        "pu_to_poh_msh_non_keyshipper": ["A3:H"],
        "pu_to_poh_msh_b2b_all_b2c_cold": ["A3:H"],
        "no_success_rate_rts_shopee_laz_other": ["A3:F"],
        "no_rsvn_completed_b2b_all_b2c_cold": ["A3:D"],
        "no_attempt_rate_keyshipper": ["A3:D"],
        "pst_itv_keyshipper": ["A3:D"],
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
            "param_poh_type_shipper": "POH type shipper",
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
                {"id": "8ea5d996-fdc4-6822-b89f-9f37eadd275c", "type": "string/=", "value": "driver_type", "target": ["dimension", ["template-tag", "courier_type"]]},
                {"id": "c142f377-ebaa-4f51-a4a8-655ce6553377", "type": "string/=", "value": "bd_shipper", "target": ["dimension", ["template-tag", "shipper_id"]]},
                {"id": "4998d505-7345-4e03-adc3-bdc5544bdfa8", "type": "string/=", "value": ["7474545", "216977", "341107"], "target": ["dimension", ["template-tag", "parent_id_coalesce"]]}
            ],
        },

        "no_rsvn_completed_key_shipper": {
            "url": "https://metabase.ninjavan.co/api/card/122256/query/json",
            "report_type": "fm",
            "common_params_template": [
                {"id": "190fb3a4-e6cb-4b4e-a78b-f4acb7cc5448", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
                {"id": "26473b49-9801-4240-ade1-6c07b7851c2a", "type": "date/single", "value": "start_end", "target": ["variable", ["template-tag", "start_date"]]},
                {"id": "8d72da7f-6a48-4384-a283-a1c81db37e2d", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "end_date"]]},
                {"id": "cd9e0dbe-b027-4a2a-bb92-bf8175c59aa1", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "is_fm_hub"]]},
                {"id": "f1fca7d5-bddb-42ce-9771-1f17b2c6a1ec", "type": "string/=", "value": "driver_type", "target": ["dimension", ["template-tag", "route_driver_type"]]},
                {"id": "f72285e9-4c7f-4b94-9b22-9cf8c929946f", "type": "number/=", "value": [1], "target": ["variable", ["template-tag", "nv_not_liable"]]},
                {"id": "ecfc3da2-aca6-4303-bb42-aa3f9a21810d", "type": "string/contains", "value": ["B2BR"], "target": ["dimension", ["template-tag", "pickup_tags"]], "options": {"case-sensitive": False}},
                {"id": "6980e48f-126e-48d9-a0d3-da79bbd63751", "type": "number/=", "value": "fsbd", "target": ["dimension", ["template-tag", "shipper_id"]]}
                # {"id": "52e3d080-5c98-4416-aa1f-dc590efa3d3c", "type": "string/=", "value": key_shipper_list, "target": ["dimension", ["template-tag", "sf_parent_acc_id_coalesce"]]},
                # {"id": "e6bb5201-d1b8-46aa-9b98-e2af5fe6578d", "type": "string/=", "value": ["Restock"], "target": ["dimension", ["template-tag", "sf_nv_product_line"]]},
            ]
        },

        # =====================================================
        # NO ATTEMPT RATE
        # common param only
        # =====================================================
        "no_attempt_rate": {
            "url": "PASTE_URL_NO_ATTEMPT_RATE",
            "report_type": "fm",
            "common_params_template": [
                {"id": "PASTE_START_DATE_ID", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "PASTE_END_DATE_ID", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "PASTE_AGGR_ID", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
            ],
        },

        # =====================================================
        # PST ITV
        # common + b2b_cc + fsbd
        # =====================================================
        "pst_itv": {
            "url": "PASTE_URL_PST_ITV",
            "report_type": "fm",
            "common_params_template": [
                {"id": "PASTE_START_DATE_ID", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "PASTE_END_DATE_ID", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "PASTE_AGGR_ID", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {"id": "PASTE_B2B_CC_PARAM_ID", "type": "string/=", "value": "b2b_cc", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
                "fsbd": [
                    {"id": "PASTE_FSBD_PARAM_ID", "type": "string/=", "value": "fsbd", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
            },
        },

        # =====================================================
        # ROT
        # common + b2b_cc
        # =====================================================
        "rot": {
            "url": "PASTE_URL_ROT",
            "report_type": "fm",
            "common_params_template": [
                {"id": "PASTE_START_DATE_ID", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "PASTE_END_DATE_ID", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "PASTE_AGGR_ID", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {"id": "PASTE_B2B_CC_PARAM_ID", "type": "string/=", "value": "b2b_cc", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
            },
        },

        # =====================================================
        # LND
        # common + b2b_cc
        # =====================================================
        "lnd": {
            "url": "PASTE_URL_LND",
            "report_type": "fm",
            "common_params_template": [
                {"id": "PASTE_START_DATE_ID", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "PASTE_END_DATE_ID", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "PASTE_AGGR_ID", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {"id": "PASTE_B2B_CC_PARAM_ID", "type": "string/=", "value": "b2b_cc", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
            },
        },

        # =====================================================
        # POPA VALIDITY
        # common + lazada + bd + fs + fsbd_lazada
        # =====================================================
        "popa_validity": {
            "url": "PASTE_URL_POPA_VALIDITY",
            "report_type": "fm",
            "common_params_template": [
                {"id": "PASTE_START_DATE_ID", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "PASTE_END_DATE_ID", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "PASTE_AGGR_ID", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
            ],
            "shipper_params_template": {
                "lazada": [
                    {"id": "PASTE_LAZADA_PARAM_ID", "type": "string/=", "value": "lazada", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
                "bd": [
                    {"id": "PASTE_BD_PARAM_ID", "type": "string/=", "value": "bd", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
                "fs": [
                    {"id": "PASTE_FS_PARAM_ID", "type": "string/=", "value": "fs", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
                "fsbd_lazada": [
                    {"id": "PASTE_FSBD_LAZADA_PARAM_ID", "type": "string/=", "value": "fsbd_lazada", "target": ["dimension", ["template-tag", "shipper_id"]]},
                ],
            },
        },

        # =====================================================
        # ASSIGN INACCURACY
        # common param only
        # =====================================================
        "assign_inaccuracy": {
            "url": "PASTE_URL_ASSIGN_INACCURACY",
            "report_type": "fm",
            "common_params_template": [
                {"id": "PASTE_START_DATE_ID", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "PASTE_END_DATE_ID", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "PASTE_AGGR_ID", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
            ],
        },

        # =====================================================
        # ASSIGN STREAMLINE
        # common param only
        # =====================================================
        "assign_streamline": {
            "url": "PASTE_URL_ASSIGN_STREAMLINE",
            "report_type": "fm",
            "common_params_template": [
                {"id": "PASTE_START_DATE_ID", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "PASTE_END_DATE_ID", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "PASTE_AGGR_ID", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
            ],
        },

        # =====================================================
        # 4W PRODUCTIVITY
        # common param only
        # =====================================================
        "four_w_productivity": {
            "url": "PASTE_URL_4W_PRODUCTIVITY",
            "report_type": "fm",
            "common_params_template": [
                {"id": "PASTE_START_DATE_ID", "type": "date/single", "value": "start_date", "target": ["variable", ["template-tag", "START_DATE"]]},
                {"id": "PASTE_END_DATE_ID", "type": "date/single", "value": "end_date", "target": ["variable", ["template-tag", "END_DATE"]]},
                {"id": "PASTE_AGGR_ID", "type": "category", "value": ["month"], "target": ["variable", ["template-tag", "aggr"]]},
            ],
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
