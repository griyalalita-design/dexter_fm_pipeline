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
            "raw_data_volume": "Raw Data Volume",
            "staff_list": "Staff List",
            "recipients":"recipients",
            "master_tracker_by_hub": "Master Tracker by Hub",
        },
        # Range yang di-clear saat Day 1 (sesuaikan)
        "clear_ranges": {
            "raw_data_otif":  ["C4:J","O4:X","AC4:AH","AL4:AQ","AV4:AZ","BD4:BG","BL4:BO","BT4:BW","CB4:CE","CJ4:CM"],
            "raw_data_inter_cost": ["A4:D","I4:N","R4:W","AA4:AF"],
            "raw_data_cost": ["B3:K","L3:T","V3:AF"],
            "raw_data_assign": ["A4:E","G4:K","M4:R","V4:Y","AE4:AF"],
            "raw_data_volume": ["A3:D"],
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
        "no_success_rate_rts_shopee": "NO Success Rate RTS Shopee",
        "no_success_rate_rts_others": "NO Success Rate RTS Others",
        "no_success_rate_rts_lazada": "NO Success Rate RTS Lazada",
        "no_rsvn_completed_b2b_all_b2c_cold": "NO RSVN Completed B2B All & B2C Cold",
        "no_attempt_rate_keyshipper": "NO Attempt Rate Keyshipper",
        "pst_itv_keyshipper": "PST ITV Keyshipper",
        "rot_b2b_all_b2c_cold": "RoT B2B All & B2C Cold",
        "popa_validity_lazada": "POPA Validity Lazada",
        "popa_validity_aggregator": "POPA Validity Aggregator",
        "popa_validity_fs": "POPA Validity FS",
        "popa_validity_fsbd_lazada": "POPA Validity FSBD Lazada",
        "lnd_rate_b2b_all_b2c_cold": "LnD Rate B2B All & B2C Cold",
        "lnd_rate": "LnD Rate",
        "4w_productivity": "4W Productivity",
        "assignment_inaccuracy": "Assignment Inaccuracy",
        "assignment_stream": "Assignment Stream",
        "eligibility_volume": "Eligibility (Volume)",
        "eki_no_hit": "EKI no hit",
        "staff_list": "Staff List"
    },

    # isi range sendiri nanti
    "clear_ranges": {
        "pu_to_poh_msh_keyshipper": ["A3:H"],
        "pu_to_poh_msh_non_keyshipper": ["A3:H"],
        "pu_to_poh_msh_b2b_all_b2c_cold": ["A3:H"],
        "no_success_rate_rts_shopee": ["A3:F"],
        "no_success_rate_rts_others": ["A3:F"],
        "no_success_rate_rts_lazada": ["A3:F"],
        "no_rsvn_completed_b2b_all_b2c_cold": ["A3:D"],
        "no_attempt_rate_keyshipper": ["A3:D"],
        "pst_itv_keyshipper": ["A3:D"],
        "rot_b2b_all_b2c_cold": ["A3:D"],
        "popa_validity_lazada": ["A3:F"],
        "popa_validity_aggregator": ["A3:F"],
        "popa_validity_fs": ["A3:F"],
        "popa_validity_fsbd_lazada": ["A3:F"],
        "lnd_rate_b2b_all_b2c_cold": ["A3:D"],
        "lnd_rate": ["A3:D"],
        "4w_productivity": ["A3:I"],
        "assignment_inaccuracy": ["A3:E"],
        "assignment_stream": ["A3:F"],
        "eligibility_volume": ["A3"D],
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
    "poa": {
        "poa_iv_1": {
            "url": "https://metabase.ninjavan.co/api/card/122270/query/json",
            "report_type": "poa",
            "common_params_template": [
                {
                    "id": "e6c527e6-8587-41ef-ba1e-223fadbca52a",
                    "type": "date/single",
                    "value_key": "start_date",
                    "target": ["variable", ["template-tag", "start_date"]],
                },
                {
                    "id": "e33b0e69-95c3-4fc3-9e08-2bce46b52ebe",
                    "type": "date/single",
                    "value_key": "end_date",
                    "target": ["variable", ["template-tag", "end_date"]],
                },
                {
                    "id": "5cfead49-71f9-45f9-86b8-d52079f5c4dd",
                    "type": "category",
                    "value": ["month"],
                    "target": ["variable", ["template-tag", "aggr"]],
                },
                {
                    "id": "74ebbf84-d66c-49c6-9d30-c1f260297ed4",
                    "type": "string/=",
                    "value": [
                        "BDO-BDO", "CBN-CBN", "KNO-KNO", "PDG-PDG", "PKU-PKU",
                        "PLM-PLM", "SOC-SOC", "SRG-SRG", "SUB-SUB", "TKG-TKG", "MAC-MAC"
                    ],
                    "target": ["dimension", ["template-tag", "crossdock_orig_hub"]],
                },
                {
                    "id": "bbb8cd83-b7bd-4ce2-8d44-74c0f6e98704",
                    "type": "number/=",
                    "value": ["120"],
                    "target": ["variable", ["template-tag", "Parameter"]],
                },
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {
                        "id": "f00e3394-9239-4262-89cd-8e735f249c9a",
                        "type": "string/=",
                        "value_key": "b2b_cc",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "fsbd": [
                    {
                        "id": "f9ba1af7-0782-4239-9b17-fa26bfb9150a",
                        "type": "string/=",
                        "value": ["7474545"],
                        "target": ["dimension", ["template-tag", "parent_id_coalesce"]],
                    },
                    {
                        "id": "f00e3394-9239-4262-89cd-8e735f249c9a",
                        "type": "string/=",
                        "value_key": "fsbd",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "others": [
                    {
                        "id": "f9ba1af7-0782-4239-9b17-fa26bfb9150a",
                        "type": "string/=",
                        "value": ["216977", "341107", "341121"],
                        "target": ["dimension", ["template-tag", "parent_id_coalesce"]],
                    }
                ],
            },
        },

        "poa_iv_2": {
            "url": "https://metabase.ninjavan.co/api/card/122273/query/json",
            "report_type": "poa",
            "common_params_template": [
                {
                    "id": "e6c527e6-8587-41ef-ba1e-223fadbca52a",
                    "type": "date/single",
                    "value_key": "start_date",
                    "target": ["variable", ["template-tag", "start_date"]],
                },
                {
                    "id": "e33b0e69-95c3-4fc3-9e08-2bce46b52ebe",
                    "type": "date/single",
                    "value_key": "end_date",
                    "target": ["variable", ["template-tag", "end_date"]],
                },
                {
                    "id": "2bbcd4b3-21ed-4c12-97ba-dcb26f4e9579",
                    "type": "category",
                    "value": ["month"],
                    "target": ["variable", ["template-tag", "aggr"]],
                },
                {
                    "id": "74ebbf84-d66c-49c6-9d30-c1f260297ed4",
                    "type": "string/=",
                    "value": [
                        "BDO-BDO", "CBN-CBN", "KNO-KNO", "PDG-PDG", "PKU-PKU",
                        "PLM-PLM", "SOC-SOC", "SRG-SRG", "SUB-SUB", "TKG-TKG", "MAC-MAC"
                    ],
                    "target": ["dimension", ["template-tag", "crossdock_orig_hub"]],
                },
                {
                    "id": "bbb8cd83-b7bd-4ce2-8d44-74c0f6e98704",
                    "type": "number/=",
                    "value": ["120"],
                    "target": ["variable", ["template-tag", "Parameter"]],
                },
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {
                        "id": "6a00c9bf-3e5b-4796-823b-fc5debd9eb5a",
                        "type": "string/=",
                        "value_key": "b2b_cc",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "fsbd": [
                    {
                        "id": "9668505e-c96a-4dc3-bd52-86cf2d2a9604",
                        "type": "string/=",
                        "value": ["7474545"],
                        "target": ["dimension", ["template-tag", "parent_id_coalesce"]],
                    },
                    {
                        "id": "6a00c9bf-3e5b-4796-823b-fc5debd9eb5a",
                        "type": "string/=",
                        "value_key": "fsbd",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "others": [
                    {
                        "id": "9668505e-c96a-4dc3-bd52-86cf2d2a9604",
                        "type": "string/=",
                        "value": ["216977", "341107", "341121"],
                        "target": ["dimension", ["template-tag", "parent_id_coalesce"]],
                    }
                ],
            },
        },

        "poa_iv_3": {
            "url": "https://metabase.ninjavan.co/api/card/122275/query/json",
            "report_type": "poa",
            "common_params_template": [
                {
                    "id": "e6c527e6-8587-41ef-ba1e-223fadbca52a",
                    "type": "date/single",
                    "value_key": "start_date",
                    "target": ["variable", ["template-tag", "start_date"]],
                },
                {
                    "id": "e33b0e69-95c3-4fc3-9e08-2bce46b52ebe",
                    "type": "date/single",
                    "value_key": "end_date",
                    "target": ["variable", ["template-tag", "end_date"]],
                },
                {
                    "id": "c21a3d7d-bb56-4431-bd8e-0ef067551bc9",
                    "type": "category",
                    "value": ["month"],
                    "target": ["variable", ["template-tag", "aggr"]],
                },
                {
                    "id": "74ebbf84-d66c-49c6-9d30-c1f260297ed4",
                    "type": "string/=",
                    "value": [
                        "BDO-BDO", "CBN-CBN", "KNO-KNO", "PDG-PDG", "PKU-PKU",
                        "PLM-PLM", "SOC-SOC", "SRG-SRG", "SUB-SUB", "TKG-TKG", "MAC-MAC"
                    ],
                    "target": ["dimension", ["template-tag", "crossdock_orig_hub"]],
                },
                {
                    "id": "bbb8cd83-b7bd-4ce2-8d44-74c0f6e98704",
                    "type": "number/=",
                    "value": ["120"],
                    "target": ["variable", ["template-tag", "Parameter"]],
                },
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {
                        "id": "fd7ebc96-a20d-4b7a-acb0-6177809bf8d5",
                        "type": "string/=",
                        "value_key": "b2b_cc",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "fsbd": [
                    {
                        "id": "67cb1932-3608-4869-951b-879c6373c09d",
                        "type": "string/=",
                        "value": ["7474545"],
                        "target": ["dimension", ["template-tag", "parent_id_coalesce"]],
                    },
                    {
                        "id": "fd7ebc96-a20d-4b7a-acb0-6177809bf8d5",
                        "type": "string/=",
                        "value_key": "fsbd",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "others": [
                    {
                        "id": "67cb1932-3608-4869-951b-879c6373c09d",
                        "type": "string/=",
                        "value": ["216977", "341107", "341121"],
                        "target": ["dimension", ["template-tag", "parent_id_coalesce"]],
                    }
                ],
            },
        },

        "poa_iv_4": {
            "url": "https://metabase.ninjavan.co/api/card/122277/query/json",
            "report_type": "poa",
            "common_params_template": [
                {
                    "id": "e6c527e6-8587-41ef-ba1e-223fadbca52a",
                    "type": "date/single",
                    "value_key": "start_date",
                    "target": ["variable", ["template-tag", "start_date"]],
                },
                {
                    "id": "e33b0e69-95c3-4fc3-9e08-2bce46b52ebe",
                    "type": "date/single",
                    "value_key": "end_date",
                    "target": ["variable", ["template-tag", "end_date"]],
                },
                {
                    "id": "f37ffd8a-d39f-45be-acda-eaf7474886a9",
                    "type": "category",
                    "value": ["month"],
                    "target": ["variable", ["template-tag", "aggr"]],
                },
                {
                    "id": "74ebbf84-d66c-49c6-9d30-c1f260297ed4",
                    "type": "string/=",
                    "value": [
                        "BDO-BDO", "CBN-CBN", "KNO-KNO", "PDG-PDG", "PKU-PKU",
                        "PLM-PLM", "SOC-SOC", "SRG-SRG", "SUB-SUB", "TKG-TKG", "MAC-MAC"
                    ],
                    "target": ["dimension", ["template-tag", "crossdock_orig_hub"]],
                },
                {
                    "id": "bbb8cd83-b7bd-4ce2-8d44-74c0f6e98704",
                    "type": "number/=",
                    "value": ["120"],
                    "target": ["variable", ["template-tag", "Parameter"]],
                },
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {
                        "id": "eb2dd4a9-f423-4ba1-9984-4a3f094d0d86",
                        "type": "string/=",
                        "value_key": "b2b_cc",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "fsbd": [
                    {
                        "id": "4c3ec4a2-149a-4f43-932e-302f4397a275",
                        "type": "string/=",
                        "value": ["7474545"],
                        "target": ["dimension", ["template-tag", "parent_id_coalesce"]],
                    },
                    {
                        "id": "eb2dd4a9-f423-4ba1-9984-4a3f094d0d86",
                        "type": "string/=",
                        "value_key": "fsbd",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "others": [
                    {
                        "id": "4c3ec4a2-149a-4f43-932e-302f4397a275",
                        "type": "string/=",
                        "value": ["216977", "341107", "341121"],
                        "target": ["dimension", ["template-tag", "parent_id_coalesce"]],
                    }
                ],
            },
        },
    },

    "lnd": {
        "lnd_1": {
            "url": "https://metabase.ninjavan.co/api/card/122268/query/json",
            "report_type": "lnd",
            "common_params_template": [
                {
                    "id": "e6a1e9c8-8f83-9dfd-fecb-832d67512759",
                    "type": "date/single",
                    "value_key": "start_date",
                    "target": ["variable", ["template-tag", "start"]],
                },
                {
                    "id": "e017c9c6-0345-5b57-2d2c-a99a375ec2cb",
                    "type": "date/single",
                    "value_key": "end_date",
                    "target": ["variable", ["template-tag", "end"]],
                },
                {
                    "id": "d49289f0-e6be-cdae-aaba-c025c53fe61e",
                    "type": "category",
                    "value": ["month"],
                    "target": ["variable", ["template-tag", "aggr"]],
                },
                {
                    "id": "e0a847b5-0b07-844a-c98d-5e150bcee6b7",
                    "type": "string/=",
                    "value": [
                        "BDO-BDO", "CBN-CBN", "KNO-KNO", "PDG-PDG", "PKU-PKU",
                        "PLM-PLM", "SOC-SOC", "SRG-SRG", "SUB-SUB", "TKG-TKG", "MAC-MAC"
                    ],
                    "target": ["dimension", ["template-tag", "hub_name"]],
                },
            ],
            "shipper_params_template": {
                "b2b_cc": [
                    {
                        "id": "b43a47f7-fe04-417d-8bce-ef5f111b8fa7",
                        "type": "string/=",
                        "value_key": "b2b_cc",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "fsbd": [
                    {
                        "id": "d98aa80a-0bb0-4838-af30-2b2128c6be86",
                        "type": "string/=",
                        "value": ["7474545"],
                        "target": ["dimension", ["template-tag", "parent_id"]],
                    },
                    {
                        "id": "b43a47f7-fe04-417d-8bce-ef5f111b8fa7",
                        "type": "string/=",
                        "value_key": "fsbd",
                        "target": ["dimension", ["template-tag", "shipper_id"]],
                    }
                ],
                "others": [
                    {
                        "id": "d98aa80a-0bb0-4838-af30-2b2128c6be86",
                        "type": "string/=",
                        "value": ["216977", "341107"],
                        "target": ["dimension", ["template-tag", "parent_id"]],
                    }
                ],
            },
        }
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
