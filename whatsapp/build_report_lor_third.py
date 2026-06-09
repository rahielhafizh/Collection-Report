from datetime import datetime
from general_task import *
from services.config import load_config, wait_timer, logger
import os
import time

CONFIG = load_config()


def send_third_report_lor():
    logger.info("INITIATING EXCEL REPORT LOR FOR THIRD REPORT")
    os.startfile(CONFIG["SUBMISSION_LOR_FILENAME"])
    wait_timer(CONFIG["WAIT_TIME"]["TWENTY_SECOND"])

    # PREPARING REPORT
    maximize_app_window()
    switch_to_first_sheet()
    switch_to_first_cells()

    # CHANGE REPORT SHEET
    pyautogui.hotkey("ctrl", "pagedown")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    pyautogui.hotkey("ctrl", "pagedown")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    # COPY PICTURE AS BITMAP
    switch_to_first_cells()
    switch_to_table_cells()
    capture_table_as_bitmap()
    switch_to_first_cells()

    # CLOSE FILE REPORT
    switch_to_first_sheet()
    switch_to_first_cells()
    close_unsave()
    logger.info("AUTOMATION FOR THIRD REPORT LOR WAS COMPLETED")


if __name__ == "__main__":
    logger.info(">> INITIALIZING AUTOMATION PROCESS FOR THIRD REPORT LOR")
    send_third_report_lor()
