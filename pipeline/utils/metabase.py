# ============================================================
# utils/metabase.py - Semua extract data dari Metabase
# Tidak ada transformasi di sini.
# ============================================================

import json
import os
import time
import json
from urllib.parse import quote

import pandas as pd
import requests

from config.settings import GSHEET
from utils.gsheet import get_cell_value


def get_token() -> str:
    """
    Ambil token Metabase dari env dulu.
    Kalau tidak ada, fallback ke Google Sheet config.
    """
    env_token = (os.getenv("METABASE_TOKEN") or "").strip().strip("'").strip('"')
    if env_token:
        print("Using METABASE_TOKEN from environment.")
        return env_token

    print("METABASE_TOKEN not found in environment. Fallback to Google Sheet config...")

    config_sheet = GSHEET["config"]
    token = get_cell_value(
        sheet_id=config_sheet["sheet_id"],
        tab_name=config_sheet["tabs"]["main"],
        cell=config_sheet["token_cell"],
    )

    token = (token or "").strip().strip("'").strip('"')

    if not token:
        raise ValueError("Token Metabase kosong di environment dan config sheet.")

    print("Using token from Google Sheet config.")
    return token




def tarik_metabase(url, parameters, token, desc, timeout=300, retries=3, retry_sleep=5):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Metabase-Session": token,
    }
    payload = "parameters=" + quote(json.dumps(parameters))

    last_error = None

    for attempt in range(1, retries + 1):
        print(f"Pulling {desc} (attempt {attempt}/{retries})")

        try:
            r = requests.post(url, headers=headers, data=payload, timeout=timeout)
        except requests.exceptions.ReadTimeout as e:
            last_error = e
            print(f"[{desc}] Read timeout after {timeout}s")
            if attempt < retries:
                print(f"[{desc}] retrying in {retry_sleep}s...")
                time.sleep(retry_sleep)
                continue
            return pd.DataFrame()

        except requests.exceptions.RequestException as e:
            last_error = e
            print(f"[{desc}] Request failed: {e}")
            if attempt < retries:
                print(f"[{desc}] retrying in {retry_sleep}s...")
                time.sleep(retry_sleep)
                continue
            return pd.DataFrame()

        print(f"[{desc}] status: {r.status_code}")
        print(f"[{desc}] content-type: {r.headers.get('content-type')}")

        if r.status_code != 200:
            print(f"[{desc}] FAILED body preview: {r.text[:1000]}")
            if attempt < retries and r.status_code in {500, 502, 503, 504}:
                print(f"[{desc}] retrying in {retry_sleep}s...")
                time.sleep(retry_sleep)
                continue
            return pd.DataFrame()

        try:
            data = r.json()
        except requests.exceptions.JSONDecodeError:
            print(f"[{desc}] Response is not JSON")
            print(f"[{desc}] body preview: {r.text[:1000]}")
            return pd.DataFrame()

        return pd.DataFrame(data) if data else pd.DataFrame()

    print(f"[{desc}] Final failure: {last_error}")
    return pd.DataFrame()

