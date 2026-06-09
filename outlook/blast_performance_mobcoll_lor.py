import os
import pyautogui
from datetime import datetime, timedelta
from general_task import *
from pynput.keyboard import Controller
from screen_keeper import scanning_keeper, start_keeper, stop_keeper
from services.check.capslock_checker import capslock_checking
from services.check.chrome_checker import open_outlook
from services.cleaner.clean_summary_lor_mail import clean_path
from services.config import get_month_id, load_config, logger, wait_timer
from services.duration_counter import get_duration, start_timer, stop_timer
from services.mailer.outlook_summary_lor import send_outlook_email

pyautogui.FAILSAFE = False
CONFIG = load_config()
keyboard = Controller()


def excel_config():
    logger.info("[SYSTEM] SUMMARY REPORT MOBCOLL LOR EXCEL WORKFLOW")
    os.startfile(CONFIG["WORKSOURCE_MOBCOLL_LOR"])
    wait_timer(CONFIG["WAIT_TIME"]["TWENTY_SECOND"])
    maximize_app_window()
    switch_to_first_sheet()

    # ── REFRESH DATA ──────────────────────────────────────────────────────────
    logger.info("[EXCEL] REFRESH EXCEL PROCESS")
    refresh_excel_data()
    wait_timer(CONFIG["WAIT_TIME"]["TWO_MINUTE"])
    handle_refresh_process()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_MINUTE"])
    accept_refresh()
    switch_to_first_cells()

    # ── NAVIGATE TO SUMMARY SHEET ─────────────────────────────────────────────
    switch_to_right_sheet()
    switch_to_right_sheet()
    switch_to_first_cells()

    # ── COPY SHEET TO NEW WORKBOOK ────────────────────────────────────────────
    select_sheet_down()
    move_or_copy_menu()
    move_or_copy_as_newbook()
    wait_timer(CONFIG["WAIT_TIME"]["THIRTY_SECOND"])

    move_cell_horizontal()
    switch_to_first_cells()

    # ── BREAK EXTERNAL LINKS ──────────────────────────────────────────────────
    logger.info("[EXCEL] BREAK EXTERNAL LINKS")
    break_excel_link()
    wait_timer(CONFIG["WAIT_TIME"]["THIRTY_SECOND"])
    handle_breaklink_process()
    move_cursor_figure_eight()
    escaping()

    # ── CAPTURE TABLE AS PICTURE ──────────────────────────────────────────────
    switch_to_first_cells()
    switch_to_table_cells()
    capture_table_as_picture()
    switch_to_first_cells()

    # ── SAVE NEW WORKBOOK ─────────────────────────────────────────────────────
    save_new_book()
    pyautogui.write(CONFIG["SUBMISSION_LOR_MAIL"])
    confirm()
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])

    set_new_book_name()
    today = datetime.now() - timedelta(days=1)
    month_idn_title = get_month_id(today.strftime("%B"), case="title")
    lor_filename = f"Summary Report Mobcoll LoR (Periode {month_idn_title})"
    pyautogui.write(lor_filename, interval=0.05)
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
    performance_year = today.strftime("%Y")
    month_idn_title = get_month_id(today.strftime("%B"), case="title")

    subject_email = f"Summary Report Penugasan & Kunjungan Mobcoll LoR Periode {month_idn_title} {performance_year}"

    core_email = f"""Dear All,

Dengan hormat,

Berikut terlampir Summary Report Penugasan & Kunjungan Mobile Collection LoR pada periode {month_idn_title} {performance_year}

Catatan
- Laporan ini dihasilkan secara otomatis dan disusun oleh sistem.
Seluruh data harap diperhatikan dan dievaluasi kembali.

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
    logger.info("[SYSTEM] START SUMMARY REPORT MOBCOLL LOR")
    start_timer()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    # ── PRE-FLIGHT CHECKS ─────────────────────────────────────────────────────
    capslock_checking()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    scanning_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    stop_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    clean_path(target_folder=CONFIG["SUBMISSION_LOR_MAIL"])
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
    logger.info("[SYSTEM] SUMMARY REPORT MOBCOLL LOR SENT")

    # ── FINALISE ──────────────────────────────────────────────────────────────
    stop_timer()
    execution_time = get_duration()
    logger.info(f"[SYSTEM] TOTAL EXECUTION TIME : {execution_time}")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    logger.warning("[SYSTEM] RESTARTING SCREEN KEEPER")
    start_keeper()
