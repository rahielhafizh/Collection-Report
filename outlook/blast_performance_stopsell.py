import os
import sys
from datetime import datetime, timedelta

# Menyesuaikan path untuk mengimpor modul dari root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

import pyautogui
from pynput.keyboard import Controller

from general_task import *
from screen_keeper import scanning_keeper, start_keeper, stop_keeper
from services.check.capslock_checker import capslock_checking
from services.check.chrome_checker import open_outlook
from services.cleaner.clean_summary_report_stopsell import clean_path
from services.config import get_month_id, load_config, logger, wait_timer
from services.duration_counter import get_duration, start_timer, stop_timer
from services.mailer.outlook_summary_report_stopsell import send_outlook_email

pyautogui.FAILSAFE = False
CONFIG = load_config()
keyboard = Controller()


def excel_config():
    logger.info("[SYSTEM] SUMMARY STOPSELL REPORT EXCEL WORKFLOW")
    os.startfile(CONFIG["WORKSOURCE_STOPSELL"])
    wait_timer(CONFIG["WAIT_TIME"]["TWENTY_SECOND"])
    maximize_app_window()
    switch_to_first_sheet()

    # ── REFRESH DATA ──────────────────────────────────────────────────────────
    refresh_excel_data()
    wait_timer(CONFIG["WAIT_TIME"]["TWO_MINUTE"])
    accept_refresh()

    # ── NAVIGATE TO SUMMARY SHEET ─────────────────────────────────────────────
    switch_to_right_sheet()
    switch_to_first_cells()

    # ── COPY SHEET TO NEW WORKBOOK ────────────────────────────────────────────
    select_sheet_down()
    move_or_copy_menu()
    move_or_copy_as_newbook()
    wait_timer(CONFIG["WAIT_TIME"]["FIFTEEN_SECOND"])

    switch_to_first_cells()
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])

    # ── BREAK EXTERNAL LINKS ──────────────────────────────────────────────────
    break_excel_link()
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.hotkey("esc")
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])

    # ── CAPTURE TABLE AS PICTURE ──────────────────────────────────────────────
    switch_to_right_sheet()
    switch_to_first_cells()
    switch_to_table_cells()
    capture_table_as_picture()
    switch_to_first_cells()

    # ── SAVE NEW WORKBOOK ─────────────────────────────────────────────────────
    save_new_book()
    pyautogui.write(CONFIG["SUBMISSION_STOPSELL"])
    confirm()
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])

    set_new_book_name()
    today = datetime.now() - timedelta(days=1)
    report_stopsell_day = today.strftime("%d")
    month_idn_title = get_month_id(today.strftime("%B"), case="title")
    stopsell_filename = f"Summary Penugasan & Kunjungan Cabang Stop Sell ({report_stopsell_day} {month_idn_title})"
    pyautogui.write(stopsell_filename, interval=0.05)
    confirm()
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    closing_tab()
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])

    logger.info("[EXCEL] CLOSE WORKSOURCE FILE")
    switch_to_first_sheet()
    switch_to_first_cells()
    close_unsave()


def send_email():
    outlook_recipients = ["asset.mgmt@sfi.co.id"]
    secondary_recipients = ["collho.3@sfi.co.id", "herberth.simbolon@sfi.co.id"]

    today = datetime.now() - timedelta(days=1)
    report_stopsell_day = today.strftime("%d")
    performance_year = today.strftime("%Y")
    month_idn_title = get_month_id(today.strftime("%B"), case="title")

    subject_email = (
        f"Summary Penugasan & Kunjungan Cabang Stop Sell As Of | "
        f"{report_stopsell_day} {month_idn_title} {performance_year}"
    )

    core_email = f"""Dear All,

Dengan hormat,

Berikut terlampir Summary Penugasan & Kunjungan Cabang Stop Sell As Of {month_idn_title} {performance_year}

Catatan
- Laporan ini dihasilkan secara otomatis & disusun oleh sistem.
Seluruh data harap diperhatikan & dievaluasi kembali.

"""

    footer_template = """


Hormat kami,
Asset Management Division
Collection HO - PT Suzuki Finance Indonesia
"""

    send_outlook_email(
        outlook_recipients,
        secondary_recipients,
        subject_email,
        core_email,
        footer_template,
    )


if __name__ == "__main__":
    logger.info("[SYSTEM] START SUMMARY STOPSELL REPORT")
    start_timer()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    # ── PRE-FLIGHT CHECKS ─────────────────────────────────────────────────────
    capslock_checking()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    scanning_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    stop_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    clean_path(target_folder=CONFIG["SUBMISSION_STOPSELL"])
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    # ── PRE-FLIGHT OUTLOOK ────────────────────────────────────────────────────
    open_outlook()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    closing_tab()
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])

    # ── EXCEL PROCESSING ──────────────────────────────────────────────────────
    excel_config()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    # ── EMAIL DISPATCH ────────────────────────────────────────────────────────
    send_email()
    logger.info("[SYSTEM] SUMMARY STOPSELL REPORT SENT")

    # ── FINALISE ──────────────────────────────────────────────────────────────
    stop_timer()
    execution_time = get_duration()
    logger.info(f"[SYSTEM] TOTAL EXECUTION TIME : {execution_time}")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    logger.warning("[SYSTEM] RESTARTING SCREEN KEEPER")
    start_keeper()
