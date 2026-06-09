import os
import pyautogui
from datetime import datetime, timedelta
from general_task import *
from pynput.keyboard import Controller
from screen_keeper import scanning_keeper, start_keeper, stop_keeper
from services.check.capslock_checker import capslock_checking
from services.check.chrome_checker import open_outlook
from services.cleaner.clean_summary_ar_tod import clean_path
from services.config import get_month_id, load_config, logger, wait_timer
from services.duration_counter import get_duration, start_timer, stop_timer
from services.mailer.outlook_summary_ar_tod import send_outlook_email

pyautogui.FAILSAFE = False
CONFIG = load_config()
keyboard = Controller()


def excel_config():
    logger.info("[EXCEL] OPEN WORKSOURCE FILE")
    os.startfile(CONFIG["WORKSOURCE_AR_TOD"])
    wait_timer(CONFIG["WAIT_TIME"]["TWENTY_SECOND"])
    maximize_app_window()
    switch_to_first_sheet()

    # ── NAVIGATE TO SUMMARY SHEET ─────────────────────────────────────────────
    for _ in range(4):
        switch_to_right_sheet()
    switch_to_first_cells()

    # ── REFRESH DATA ──────────────────────────────────────────────────────────
    logger.info("[EXCEL] REFRESH EXCEL PROCESS")
    refresh_excel_data()
    wait_timer(CONFIG["WAIT_TIME"]["THREEHALF_MINUTE"])
    handle_refresh_process()
    wait_timer(CONFIG["WAIT_TIME"]["THREEHALF_MINUTE"])
    accept_refresh()
    switch_to_first_cells()

    # ── COPY SHEET TO NEW WORKBOOK ────────────────────────────────────────────
    logger.info("[EXCEL] MOVE AND COPY WORKBOOK")
    select_sheet_performance()
    move_or_copy_menu()
    move_or_copy_as_newbook()
    wait_timer(CONFIG["WAIT_TIME"]["FOUR_MINUTE"])
    handle_move_copy_process()
    wait_timer(CONFIG["WAIT_TIME"]["FOUR_MINUTE"])
    handle_move_copy_process()
    move_cursor_figure_eight()

    logger.info("[EXCEL] NAVIGATE IN NEW WORKBOOK")
    switch_to_right_sheet()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    switch_to_first_cells()
    move_cell_horizontal()
    switch_to_first_sheet()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    # ── BREAK EXTERNAL LINKS ──────────────────────────────────────────────────
    logger.info("[EXCEL] BREAK EXTERNAL LINKS")
    move_cursor_figure_eight()
    break_excel_link()
    wait_timer(CONFIG["WAIT_TIME"]["THREE_MINUTE"])
    handle_breaklink_process()
    wait_timer(CONFIG["WAIT_TIME"]["THREE_MINUTE"])
    handle_breaklink_process()
    move_cursor_figure_eight()
    escaping()

    # ── CAPTURE TABLE AS PICTURE ──────────────────────────────────────────────
    logger.info("[EXCEL] CAPTURE TABLE AS PICTURE")
    switch_to_first_sheet()
    move_cursor_figure_eight()
    switch_to_first_cells()
    switch_to_table_cells()
    capture_table_as_picture()
    switch_to_first_cells()

    # ── SAVE NEW WORKBOOK ─────────────────────────────────────────────────────
    logger.info("[EXCEL] SAVE NEW WORKBOOK")
    save_new_book()
    pyautogui.write(CONFIG["SUBMISSION_AR_TOD"])
    confirm()
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])

    set_new_book_name()
    today = datetime.now() - timedelta(days=1)
    ar_tod_day = today.strftime("%d")
    month_idn_title = get_month_id(today.strftime("%B"), case="title")
    tod_filename = f"Summary Performance AR & TOD - {ar_tod_day} {month_idn_title}"
    logger.info(f"[EXCEL] FILENAME : {tod_filename}")
    pyautogui.write(tod_filename, interval=0.05)
    confirm()
    wait_timer(CONFIG["WAIT_TIME"]["THIRTY_SECOND"])

    # ── CLOSE WORKBOOKS ───────────────────────────────────────────────────────
    move_cursor_figure_eight()
    closing_tab()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_MINUTE"])

    logger.info("[EXCEL] CLOSE WORKSOURCE FILE")
    move_cursor_figure_eight()
    switch_to_first_sheet()
    switch_to_first_cells()
    close_unsave()


def send_email():
    outlook_recipients = ["asset.mgmt@sfi.co.id"]
    secondary_recipients = ["collho.3@sfi.co.id", "herberth.simbolon@sfi.co.id"]

    today = datetime.now() - timedelta(days=1)
    ar_tod_day = today.strftime("%d")
    month_idn_title = get_month_id(today.strftime("%B"), case="title")

    subject_email = f"Summary Performance AR & TOD | {ar_tod_day} {month_idn_title}"

    core_email = f"""Dear All,

Dengan hormat,

Berikut terlampir Summary Performance AR & TOD pada {ar_tod_day} {month_idn_title}

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
    logger.info("[SYSTEM] START SUMMARY PERFORMANCE AR & TOD REPORT")
    start_timer()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    # ── PRE-FLIGHT CHECKS ─────────────────────────────────────────────────────
    capslock_checking()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    scanning_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    stop_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    clean_path(target_folder=CONFIG["SUBMISSION_AR_TOD"])
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
    logger.info("[SYSTEM] SUMMARY PERFORMANCE AR & TOD REPORT SENT")

    # ── FINALISE ──────────────────────────────────────────────────────────────
    stop_timer()
    execution_time = get_duration()
    logger.info(f"[SYSTEM] TOTAL EXECUTION TIME : {execution_time}")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    logger.warning("[SYSTEM] RESTARTING SCREEN KEEPER")
    start_keeper()
