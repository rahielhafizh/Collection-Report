from screen_keeper import scanning_keeper, start_keeper, stop_keeper
from services.check.capslock_checker import capslock_checking
from services.config import load_config, logger, wait_timer
from services.duration_counter import get_duration, start_timer, stop_timer
from services.report.lor.dispatcher import (
    dispatch_area_report,
    dispatch_as_of_report,
    dispatch_today_report,
)
from services.report.lor.excel_processor import refresh_workbook


CONFIG = load_config()


def dispatch_sequence_lor() -> None:
    if not dispatch_area_report():
        logger.error("[LOR] AREA REPORT FAILED — SEQUENCE ABORTED")
        return
    logger.info("[LOR] AREA REPORT DISPATCHED")

    if not dispatch_as_of_report():
        logger.error("[LOR] AS-OF REPORT FAILED — SEQUENCE ABORTED")
        return
    logger.info("[LOR] AS-OF REPORT DISPATCHED")

    if not dispatch_today_report():
        logger.error("[LOR] TODAY REPORT FAILED")
        return
    logger.info("[LOR] TODAY REPORT DISPATCHED")


if __name__ == "__main__":
    logger.info("[SYSTEM] START LOR REPORT GROUP DELIVERY")
    start_timer()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    capslock_checking()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    scanning_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    stop_keeper()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    refresh_workbook()
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    dispatch_sequence_lor()
    logger.info("[SYSTEM] LOR REPORT GROUP DELIVERY COMPLETE")

    stop_timer()
    execution_time = get_duration()
    logger.info(f"[SYSTEM] TOTAL EXECUTION TIME: {execution_time}")
    wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])
    logger.warning("[SYSTEM] RESTARTING SCREEN KEEPER")
    start_keeper()
