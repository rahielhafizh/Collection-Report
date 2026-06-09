import time
from datetime import datetime
from services.config import load_config, wait_timer, logger
from services.whatsapp_sender import send_to_group
from whatsapp.build_report_lor_first import send_first_report_lor
from whatsapp.build_report_lor_second import send_second_report_lor
from whatsapp.build_report_lor_third import send_third_report_lor


CONFIG = load_config()


def send_alda_report():
    logger.info("[ALDA] INITIATING REPORT DISPATCH")
    group_link = CONFIG.get("ASSET_GROUP")
    try:
        current_datetime = datetime.now()
        day = current_datetime.day
        month_name = current_datetime.strftime("%B").upper()
        year = current_datetime.year
        time_str = current_datetime.strftime("%H:%M")
        alda_date = f"{day} {month_name} {year}"
        message = f"REPORT ALDA | {alda_date} | {time_str}"
        send_to_group(group_link, message)

    except Exception as e:
        logger.error(f"[ALDA] REPORT DISPATCH FAILED: {str(e)}")
        return False


def send_cash_in_report():
    logger.info("[CASH IN] INITIATING REPORT DISPATCH")
    group_link = CONFIG.get("ASSET_GROUP")
    try:
        current_datetime = datetime.now()
        day = current_datetime.day
        month_name = current_datetime.strftime("%B")
        year = current_datetime.year
        time_str = current_datetime.strftime("%H:%M")
        cash_date = f"{day} {month_name} {year}"
        message = f"Update Cash In - {cash_date} Pukul : {time_str}"
        send_to_group(group_link, message)

    except Exception as e:
        logger.error(f"[CASH IN] REPORT DISPATCH FAILED: {str(e)}")
        return False


def senda_denda_aktif_report():
    logger.info("[DENDA AKTIF] INITIATING REPORT DISPATCH")
    group_link = CONFIG.get("ASSET_GROUP")
    try:
        current_datetime = datetime.now()
        day = current_datetime.day
        month_name = current_datetime.strftime("%B").upper()
        year = current_datetime.year
        time_str = current_datetime.strftime("%H:%M")
        denda_aktif_date = f"{day} {month_name} {year}"
        message = f"REPORT DENDA AKTIF | {denda_aktif_date} | {time_str}"
        send_to_group(group_link, message)

    except Exception as e:
        logger.error(f"[DENDA AKTIF] REPORT DISPATCH FAILED: {str(e)}")
        return False


def send_first_reports():
    logger.info("[LOR FIRST] INITIATING REPORT DISPATCH")
    group_link = CONFIG.get("ASSET_GROUP")
    try:
        send_first_report_lor()
        logger.info("[LOR FIRST] REPORT GENERATED SUCCESSFULLY")
        current_datetime = datetime.now()
        day = current_datetime.day
        month_name = current_datetime.strftime("%B").upper()
        year = current_datetime.year
        first_datetime = f"{day} {month_name} {year}"
        message = f"MOBCOLL REPORT LOR | {first_datetime} | REPORT AREA"
        result = send_to_group(group_link, message)
        if result:
            logger.info("[LOR FIRST] REPORT DISPATCHED SUCCESSFULLY")
            return True
        else:
            logger.error("[LOR FIRST] REPORT DISPATCH FAILED")
            return False

    except Exception as e:
        logger.error(f"[LOR FIRST] REPORT DISPATCH ERROR: {str(e)}")
        return False


def send_second_reports():
    logger.info("[LOR SECOND] INITIATING REPORT DISPATCH")
    group_link = CONFIG.get("ASSET_GROUP")
    try:
        send_second_report_lor()
        logger.info("[LOR SECOND] REPORT GENERATED SUCCESSFULLY")
        current_datetime = datetime.now()
        day = current_datetime.day
        month_name = current_datetime.strftime("%B").upper()
        year = current_datetime.year
        second_datetime = f"1 s/d {day} {month_name} {year}"
        message = f"AS OF REPORT LOR | {second_datetime} | AREA DAN CABANG"
        result = send_to_group(group_link, message)
        if result:
            logger.info("[LOR SECOND] REPORT DISPATCHED SUCCESSFULLY")
            return True
        else:
            logger.error("[LOR SECOND] REPORT DISPATCH FAILED")
            return False

    except Exception as e:
        logger.error(f"[LOR SECOND] REPORT DISPATCH ERROR: {str(e)}")
        return False


def send_third_reports():
    logger.info("[LOR THIRD] INITIATING REPORT DISPATCH")
    group_link = CONFIG.get("ASSET_GROUP")
    try:
        send_third_report_lor()
        logger.info("[LOR THIRD] REPORT GENERATED SUCCESSFULLY")
        current_datetime = datetime.now()
        day = current_datetime.day
        month_name = current_datetime.strftime("%B").upper()
        year = current_datetime.year
        third_datetime = f"{day} {month_name} {year}"
        message = f"TODAY REPORT LOR | {third_datetime} | AREA DAN CABANG"
        result = send_to_group(group_link, message)
        if result:
            logger.info("[LOR THIRD] REPORT DISPATCHED SUCCESSFULLY")
            return True
        else:
            logger.error("[LOR THIRD] REPORT DISPATCH FAILED")
            return False

    except Exception as e:
        logger.error(f"[LOR THIRD] REPORT DISPATCH ERROR: {str(e)}")
        return False
