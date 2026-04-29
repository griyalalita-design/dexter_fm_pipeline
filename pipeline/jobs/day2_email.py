from __future__ import annotations

import re
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta

from utils.gsheet import read_sheet, get_cell_value
from config.settings import GSHEET


SENDER_DISPLAY_NAME = "ID BI-Reporting"
SENDER_ALIAS_EMAIL = "id-bi-reporting@ninjavan.co"

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

# hardcode links
METABASE_URL = "https://docs.google.com/spreadsheets/d/1URg6lx6L8jNqxfOL0-k3VSkFECN2hnXOOwCD7OnlvJo/edit?gid=1582915729#gid=1582915729"
ARCHIVES_URL = "https://drive.google.com/drive/folders/1kqFrpkWjI1DxyIjaua4N8MXx4dJVgbQr"
PPT_URL = "https://docs.google.com/presentation/d/1ubRIFrPy4pfV00V-qYQlq-0aaOvlCN7MO4Bo-rYX2GE/edit?slide=id.g142cc6d9960_0_0#slide=id.g142cc6d9960_0_0"


def get_previous_month_label() -> str:
    months_id = [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ]
    prev_month_date = datetime.today().replace(day=1) - timedelta(days=1)
    return f"{months_id[prev_month_date.month - 1]} {prev_month_date.year}"


def is_recipient_format(value: str) -> bool:
    value = str(value or "").strip()
    pattern_with_name = r"^.+<[^<>\s@]+@[^<>\s@]+\.[^<>\s@]+>$"
    pattern_email_only = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return bool(re.match(pattern_with_name, value) or re.match(pattern_email_only, value))


def extract_email_address(value: str) -> str:
    value = str(value or "").strip()
    match = re.search(r"<([^<>\s@]+@[^<>\s@]+\.[^<>\s@]+)>$", value)
    if match:
        return match.group(1)
    return value


def get_recipients_from_sheet(spreadsheet_id: str, sheet_name: str) -> list[str]:
    df = read_sheet(spreadsheet_id, sheet_name)
    if df.empty:
        return []

    first_col = df.columns[0]
    values = df[first_col].astype(str).str.strip().tolist()
    recipients = [x for x in values if is_recipient_format(x)]

    seen = set()
    uniq = []
    for r in recipients:
        if r not in seen:
            seen.add(r)
            uniq.append(r)

    return uniq


def get_email_sender_from_config():
    config_sheet = GSHEET["config"]

    email_sender = get_cell_value(
        sheet_id=config_sheet["sheet_id"],
        tab_name=config_sheet["tabs"]["main"],
        cell="B14",
    )

    app_password_sender = get_cell_value(
        sheet_id=config_sheet["sheet_id"],
        tab_name=config_sheet["tabs"]["main"],
        cell="C14",
    )

    if not email_sender:
        raise ValueError("Email sender kosong di config sheet (B14).")
    if not app_password_sender:
        raise ValueError("App password sender kosong di config sheet (C14).")

    return email_sender, app_password_sender


def make_link(url: str, label: str, style: str) -> str:
    url = str(url or "").strip()
    if not url:
        return f"<b>{label}</b>"
    return f'<a href="{url}" target="_blank" {style}>{label}</a>'


def build_html_fm_email(
    period_label: str,
    tracker_url: str,
    metabase_url: str,
    archives_url: str,
    sanggahan_url: str,
    ppt_url: str,
) -> str:
    link_common_style = 'style="color:#1565c0;font-weight:bold;text-decoration:underline"'
    link_red_style = 'style="color:#c62828;font-weight:bold;text-decoration:underline"'

    tracker_html = make_link(tracker_url, "ID FM KPI Tracker LINK", link_common_style)
    metabase_html = make_link(metabase_url, "LINK METABASE", link_common_style)
    ppt_html = make_link(ppt_url, "link PPT", link_common_style)
    sanggahan_html = make_link(sanggahan_url, "[LINK SANGGAHAN]", link_red_style)
    archives_html = make_link(archives_url, "FM KPI Archives LINK", link_common_style)

    return f"""
    <html>
    <body style="font-family: Arial, sans-serif; font-size: 13.5px; color: #222; line-height: 1.55;">
      <p>Dear all,</p>

      <p>Berikut adalah link untuk sheet <b>FM KPI Tracker</b> periode <b>{period_label}</b>:
      {tracker_html}</p>

      <p>Berikut juga link <b>Metabase</b> yang dapat digunakan untuk menarik data secara mandiri untuk monitoring harian:
      {metabase_html}</p>

      <p><b>Note:</b></p>
      <ul>
        <li>Mulai dari <b>Juli 2025</b>, berlaku skema FM KPI baru sesuai sosialisasi ({ppt_html}).</li>
        <li>Perhitungan <b>CPP</b> akan dikalkulasi secara manual pada pertengahan bulan berikutnya.</li>
        <li>Sanggahan dibuka pada tanggal <b>2–10 setiap bulannya</b>, dan dapat diajukan melalui link berikut: {sanggahan_html}.</li>
        <li>Tracker akan di-archive setiap tanggal <b>18</b>, dan arsip performa FM KPI bulan-bulan sebelumnya dapat diakses di:
        {archives_html}</li>
      </ul>

      <p>Kepada teman-teman <b>RM, AM, Pickup Lead, & Pickup FST</b>, feel free untuk meneruskan ke tim pickup terkait apabila ada yang terlewat dan menginformasikan apabila terdapat hub baru yang belum dimasukkan ke dalam tracker ini.</p>

      <p>Regards,<br><b>BI-Reporting</b></p>
    </body>
    </html>
    """


def build_plain_text(period_label: str) -> str:
    return (
        f"Dear all,\n\n"
        f"Berikut adalah email FM KPI Progressive Tracker untuk periode {period_label}.\n\n"
        f"Regards,\n"
        f"BI-Reporting"
    )


def send_email_chunked(
    smtp_user: str,
    smtp_password: str,
    to_recipients: list[str],
    subject: str,
    html_body: str,
    plain_body: str,
    chunk_size: int = 50,
) -> None:
    context = ssl.create_default_context()

    for i in range(0, len(to_recipients), chunk_size):
        chunk = to_recipients[i:i + chunk_size]
        smtp_chunk = [extract_email_address(x) for x in chunk]

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"{SENDER_DISPLAY_NAME} <{SENDER_ALIAS_EMAIL}>"
        msg["To"] = ", ".join(chunk)

        msg.attach(MIMEText(plain_body, "plain", "utf-8"))
        msg.attach(MIMEText(html_body, "html", "utf-8"))

        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, smtp_chunk, msg.as_string())

        print(f"Sent chunk {i // chunk_size + 1}: {len(chunk)} recipients")


def run():
    print("=== FM DAY 2 EMAIL START ===")

    smtp_user, smtp_password = get_email_sender_from_config()

    recipients = get_recipients_from_sheet(
        GSHEET["tracker"]["sheet_id"],
        GSHEET["tracker"]["tabs"]["recipients"]
    )

    if not recipients:
        raise ValueError("Tab recipients kosong atau tidak ada recipient valid.")

    period_label = get_previous_month_label()
    subject = f"(ID) First Mile KPI Progressive Tracker - {period_label}"

    html_body = build_html_fm_email(
        period_label=period_label,
        tracker_url=GSHEET["tracker"]["url"],
        metabase_url=METABASE_URL,
        archives_url=ARCHIVES_URL,
        sanggahan_url=GSHEET["sanggahan"]["url"],
        ppt_url=PPT_URL,
    )

    plain_body = build_plain_text(period_label)

    print(f"Recipients count: {len(recipients)}")
    print(f"Subject: {subject}")

    send_email_chunked(
        smtp_user=smtp_user,
        smtp_password=smtp_password,
        to_recipients=recipients,
        subject=subject,
        html_body=html_body,
        plain_body=plain_body,
        chunk_size=50,
    )

    print("=== FM DAY 2 EMAIL DONE ===")


if __name__ == "__main__":
    run()
