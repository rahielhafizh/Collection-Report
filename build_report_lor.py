import os
from services.remover_lor import remove_report_lor
from services.config import load_config, wait_timer, logger
from general_task import *

CONFIG = load_config()


def launch_excel_file():
    logger.info("[SYSTEM] LAUNCHING EXCEL SOURCE FILE")
    os.startfile(CONFIG["WORKSOURCE_MOBCOLL_LOR"])
    wait_timer(CONFIG["WAIT_TIME"]["TWENTY_SECOND"])
    maximize_app_window()


def refresh_excel_data_source():
    logger.info("[DATA] REFRESHING DATA SOURCE")
    switch_to_first_sheet()
    refresh_excel_data()
    wait_timer(CONFIG["WAIT_TIME"]["THREE_MINUTE"])
    switch_to_first_cells()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_MINUTE"])
    switch_to_first_cells()


def prepare_sheet_for_copy():
    logger.info("[SYSTEM] PREPARING SHEET FOR COPY")
    pyautogui.hotkey("ctrl", "pagedown")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    pyautogui.hotkey("ctrl", "pagedown")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    select_sheet_down()


def execute_move_copy_operation():
    logger.info("[SYSTEM] EXECUTING MOVE/COPY OPERATION")
    move_or_copy_menu()
    move_or_copy_as_newbook()
    wait_timer(CONFIG["WAIT_TIME"]["THIRTY_SECOND"])
    switch_to_first_cells()
    wait_timer(CONFIG["WAIT_TIME"]["TEN_SECOND"])


def setup_new_workbook():
    logger.info("[SYSTEM] BREAKING LINKS IN NEW WORKBOOK")
    break_excel_link()
    wait_timer(CONFIG["WAIT_TIME"]["FIFTEEN_SECOND"])
    pyautogui.hotkey("esc")
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])
    switch_to_last_sheet()
    switch_to_first_sheet()
    switch_to_first_cells()


def save_lor_report_file():
    logger.info("[SYSTEM] SAVING NEW LOR REPORT FILE")
    save_new_book()

    pyautogui.write(CONFIG["SUBMISSION_LOR_WA"])
    confirm()
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])

    set_new_book_name()
    whatsapp_lor_file = r"Mobcoll_LoR_Whatsapp"
    pyautogui.write(whatsapp_lor_file, interval=0.05)
    confirm()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_MINUTE"])
    closing_tab()

    logger.info("[EXCEL] CLOSE WORKSOURCE FILE")
    switch_to_first_sheet()
    switch_to_first_cells()
    close_unsave()
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    logger.info("[SYSTEM] FILE SAVED SUCCESSFULLY")


def finalize_report_creation():
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    switch_to_last_sheet()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    switch_to_first_sheet()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    switch_to_first_cells()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    close_unsave()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    logger.info("[SYSTEM] CLEANUP AND FINAL SAVE COMPLETE")


def build_source_report_lor():
    logger.info("[SYSTEM] STARTING LOR REPORT BUILD PROCESS")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    remove_report_lor()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    logger.info("[SYSTEM] OLD REPORT FILES REMOVED")
    try:
        launch_excel_file()
        wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])

        refresh_excel_data_source()
        wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])

        prepare_sheet_for_copy()
        wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])

        execute_move_copy_operation()
        wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])

        setup_new_workbook()
        wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])

        save_lor_report_file()
        wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])

        logger.info("[SYSTEM] LOR REPORT BUILD COMPLETED SUCCESSFULLY")

    except Exception as e:
        error_msg = f"[ERROR] FAILED LOR REPORT BUILD PROCESS: {str(e)}"
        logger.error(error_msg)
        try:
            close_unsave()
        except:
            pass


if __name__ == "__main__":
    logger.info("[SYSTEM] INITIALISING LOR REPORT AUTOMATION")
    build_source_report_lor()
