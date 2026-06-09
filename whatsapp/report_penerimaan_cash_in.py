from screen_keeper import scanning_keeper, start_keeper, stop_keeper
from services.check.capslock_checker import capslock_checking
from services.config import load_config, logger, wait_timer
from services.duration_counter import get_duration, start_timer, stop_timer
from services.report.cash_in.dispatcher import dispatch_cash_in_report
from services.report.cash_in.excel_processor import process_cash_in_workbook

CONFIG = load_config()


if __name__ == "__main__":
    logger.info("[SYSTEM] START CASH IN REPORT")
    start_timer()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    capslock_checking()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    scanning_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    stop_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    process_cash_in_workbook()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    dispatch_cash_in_report()
    logger.info("[SYSTEM] CASH IN REPORT SENT")

    stop_timer()
    execution_time = get_duration()
    logger.info(f"[SYSTEM] TOTAL EXECUTION TIME: {execution_time}")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    logger.warning("[SYSTEM] RESTARTING SCREEN KEEPER")
    start_keeper()