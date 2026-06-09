import logging
import sys
import time
import random
import pyautogui
import psutil
from typing import Dict, Any, Optional
from colorlog import ColoredFormatter

_pyautogui_configured = False


# ─── LOGGER FORMATTER ─────────────────────────────────────────────────────────
class SafeColoredFormatter(ColoredFormatter):
    FALLBACK_DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

    def formatTime(
        self, record: logging.LogRecord, datefmt: Optional[str] = None
    ) -> str:
        try:
            return super().formatTime(record, datefmt)
        except (UnicodeEncodeError, ValueError, OSError):
            ct = self.converter(record.created)
            return time.strftime(self.FALLBACK_DATE_FORMAT, ct)

    def format(self, record: logging.LogRecord) -> str:
        try:
            return super().format(record)
        except UnicodeEncodeError:
            record.msg = record.msg.encode("ascii", errors="replace").decode("ascii")
            record.args = ()
            try:
                return super().format(record)
            except Exception:
                return f"[LOG] {record.levelname}: {record.getMessage()}"


# ─── CONFIGURATION LOADER ─────────────────────────────────────────────────────
def load_config() -> Dict[str, Any]:
    setup_pyautogui_config()
    return DEFAULT_CONFIG


# ─── LOGGER SETUP ─────────────────────────────────────────────────────────────
def setup_logger() -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        formatter = SafeColoredFormatter(
            fmt=(
                "\n"
                "%(log_color)s[%(asctime)s] \n"
                "• CONDITION  : %(levelname)s\n"
                "• SOURCE     : %(filename)s:%(lineno)d\n"
                "• FUNCTION   : %(funcName)s()\n"
                "• MESSAGE    : %(message)s\n"
                "\n"
                "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"
            ),
            datefmt=" 📆 %d-%m-%Y 🕒 %H:%M:%S ",
            log_colors={
                "DEBUG": "blue",
                "INFO": "green",
                "WARNING": "bold_yellow",
                "ERROR": "thin_red",
                "CRITICAL": "bold_red",
            },
        )

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)

        if hasattr(stream_handler.stream, "reconfigure"):
            try:
                # Perbaikan Pylance: Menggunakan getattr untuk menghindari error static type checking
                getattr(stream_handler.stream, "reconfigure")(errors="replace")
            except Exception:
                pass
        elif hasattr(stream_handler.stream, "buffer"):
            try:
                import io

                stream_handler.stream = io.TextIOWrapper(
                    stream_handler.stream.buffer,
                    encoding="utf-8",
                    errors="replace",
                    line_buffering=True,
                )
            except Exception:
                pass

        logger.addHandler(stream_handler)

    logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
    logging.getLogger("urllib3.util.retry").setLevel(logging.WARNING)
    logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(
        logging.WARNING
    )
    logging.getLogger("requests.packages.urllib3.util.retry").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    return logger


logger = setup_logger()


# ─── APPLICATION PATHS ────────────────────────────────────────────────────────
APPLICATION_PATHS = {
    "CHROME_PATH": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "OUTLOOK_PATH": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Outlook 2013.lnk",
}

# ─── FOLDER PATHS ─────────────────────────────────────────────────────────────
FOLDER_PATHS = {
    # SUBMISSION
    "SUBMISSION_AR_TOD": rf"C:\EL\Project\Standarized\Submission\Outlook\Performance_AR_TOD",
    "SUBMISSION_BUCKET_CURRENT": rf"C:\EL\Project\Standarized\Submission\Outlook\Performance_Bucket_Current",
    "SUBMISSION_BUCKET_OD": rf"C:\EL\Project\Standarized\Submission\Outlook\Performance_Bucket_Overdue",
    "SUBMISSION_CASH_IN": rf"C:\EL\Project\Standarized\Submission\Outlook\Penerimaan_CashIn",
    "SUBMISSION_DASHBOARD_CWO": rf"C:\EL\Project\Standarized\Submission\Outlook\Performance_CWO_WO_Estimasi_WO",
    "SUBMISSION_DENDA_AKTIF": rf"C:\EL\Project\Standarized\Submission\Outlook\Penerimaan_Denda_Aktif",
    "SUBMISSION_DENDA_ALDA": rf"C:\EL\Project\Standarized\Submission\Outlook\Penerimaan_Denda_Alda",
    "SUBMISSION_MOBCOLL": rf"C:\EL\Project\Standarized\Submission\Outlook\Perfomance_Kunjungan_Mobcoll",
    "SUBMISSION_MOBCOLL_LOR": rf"C:\EL\Project\Standarized\Submission\Outlook\Perfomance_Kunjungan_Mobcoll_LoR",
    "SUBMISSION_PERFORMANCE": rf"C:\EL\Project\Standarized\Submission\Outlook\Performance_AR_Remedial_Asset",
    "SUBMISSION_RECOVERY_WO": rf"C:\EL\Project\Standarized\Submission\Outlook\Performance_Recovery_WO",
    "SUBMISSION_STOPSELL": rf"C:\EL\Project\Standarized\Submission\Outlook\Perfomance_Kunjungan_StopSell",
    # SOURCE
    "WORKSOURCE_ALDA": rf"C:\EL\Source\Summary_Penerimaan_Denda_Alda.xlsx",
    "WORKSOURCE_AR_TOD": rf"C:\EL\Source\Summary_Performance_AR_TOD.xlsx",
    "WORKSOURCE_BUCKET_CURRENT": rf"C:\EL\Source\Summary_Performance_Bucket_Current.xlsx",
    "WORKSOURCE_BUCKET_OD": rf"C:\EL\Source\Summary_Performance_Bucket_Overdue.xlsx",
    "WORKSOURCE_CASH_IN": rf"C:\EL\Source\Summary_Penerimaan_CashIn.xlsx",
    "WORKSOURCE_DASHBOARD_CWO": rf"C:\EL\Source\Summary_Performance_CWO_WO_Estimasi_WO.xlsx",
    "WORKSOURCE_DENDA_AKTIF": rf"C:\EL\Source\Summary_Penerimaan_Denda_Aktif.xlsx",
    "WORKSOURCE_MOBCOLL": rf"C:\EL\Source\Summary_Perfomance_Kunjungan_Mobcoll.xlsx",
    "WORKSOURCE_MOBCOLL_LOR": rf"C:\EL\Source\Summary_Perfomance_Kunjungan_Mobcoll_LoR.xlsx",
    "WORKSOURCE_PERFORMANCE": rf"C:\EL\Source\Summary_Performance_AR_Remedial_Asset.xlsx",
    "WORKSOURCE_RECOVERY_WO": rf"C:\EL\Source\Summary_Performance_Recovery_WO.xlsx",
    "WORKSOURCE_STOPSELL": rf"C:\EL\Source\Summary_Perfomance_Kunjungan_StopSell.xlsx",
}

# ─── CONTACT INFORMATION ──────────────────────────────────────────────────────
CONTACT_INFO = {
    "ASSET_GROUP": "https://web.whatsapp.com/accept?code=KblwmcubP6g04LzqwooTYV",
    "ADMIN_PRIMARY": "+6281382427588",
    "PERSONAL_ONE": "+6285893093275",
    "PERSONAL_TWO": "+6281299606260",
    "PERSONAL_THREE": "+6285781690029",
    "PERSONAL_FOUR": "+6281282426399",
    "PERSONAL_FIVE": "+628988171583",
}


# ─── TIMING CONFIGURATION ─────────────────────────────────────────────────────
WAIT_TIMES = {
    # MICROSECOND PRECISION TIMERS
    "HUNDRED_MICROSECOND": 0.0001,
    "TWO_HUNDRED_MICROSECOND": 0.0002,
    "FIVE_HUNDRED_MICROSECOND": 0.0005,
    # MILLISECOND PRECISION TIMERS
    "ONE_MILLISECOND": 0.001,
    "TWO_MILLISECOND": 0.002,
    "FIVE_MILLISECOND": 0.005,
    "TEN_MILLISECOND": 0.01,
    "TWENTY_MILLISECOND": 0.02,
    "FIFTY_MILLISECOND": 0.05,
    "HUNDRED_MILLISECOND": 0.1,
    "TWO_HUNDRED_MILLISECOND": 0.2,
    # SUB-SECOND PRECISION TIMERS
    "TENTH_SECOND": 0.1,
    "EIGHTH_SECOND": 0.125,
    "QUARTER_SECOND": 0.25,
    "THIRD_SECOND": 0.33,
    "HALF_SECOND": 0.5,
    "THREE_QUARTER_SECOND": 0.75,
    # STANDARD SECOND-BASED TIMERS
    "ONE_SECOND": 1,
    "ONEHALF_SECOND": 1.5,
    "TWO_SECOND": 2,
    "TWOHALF_SECOND": 2.5,
    "THREE_SECOND": 3,
    "FOUR_SECOND": 4,
    "FIVE_SECOND": 5,
    "SIX_SECOND": 6,
    "SEVEN_SECOND": 7,
    "EIGHT_SECOND": 8,
    "NINE_SECOND": 9,
    "TEN_SECOND": 10,
    "TWELVE_SECOND": 12,
    "FIFTEEN_SECOND": 15,
    "EIGHTEEN_SECOND": 18,
    "TWENTY_SECOND": 20,
    "TWENTYFIVE_SECOND": 25,
    "THIRTY_SECOND": 30,
    "THIRTYFIVE_SECOND": 35,
    "FORTY_SECOND": 40,
    "FORTYFIVE_SECOND": 45,
    "FIFTY_SECOND": 50,
    "FIFTYFIVE_SECOND": 55,
    # MINUTE-BASED TIMERS
    "ONE_MINUTE": 60,
    "ONEHALF_MINUTE": 90,
    "TWO_MINUTE": 120,
    "TWOHALF_MINUTE": 150,
    "THREE_MINUTE": 180,
    "THREEHALF_MINUTE": 210,
    "FOUR_MINUTE": 240,
    "FIVE_MINUTE": 300,
    "SIX_MINUTE": 360,
    "SEVEN_MINUTE": 420,
    "EIGHT_MINUTE": 480,
    "NINE_MINUTE": 540,
    "TEN_MINUTE": 600,
    "TWELVE_MINUTE": 720,
    "FIFTEEN_MINUTE": 900,
    "TWENTY_MINUTE": 1200,
    "TWENTYFIVE_MINUTE": 1500,
    "THIRTY_MINUTE": 1800,
    "THIRTYFIVE_MINUTE": 2100,
    "FORTY_MINUTE": 2400,
    "FORTYFIVE_MINUTE": 2700,
    "FIFTY_MINUTE": 3000,
    "FIFTYFIVE_MINUTE": 3300,
    "SIXTY_MINUTE": 3600,
    # EXTENDED DURATION TIMERS
    "NORMAL": 1,
    "EXTENDED": 2,
    "LONG": 5,
    "VERY_LONG": 10,
    "ULTRA_LONG": 30,
}


# ─── PYAUTOGUI SETTINGS ───────────────────────────────────────────────────────
PYAUTOGUI_SETTINGS = {
    "FAILSAFE": True,
    "TRUE_CONDITION": True,
    "FALSE_CONDITION": False,
    "PAUSE": 0.1,
    "DURATION": 0.1,
    "INTERVAL": 0.05,
    "LOG_SCREENSHOTS": False,
    "SCREENSHOT_FOLDER": "screenshots",
    "MINIMUM_DURATION": 0.1,
    "MINIMUM_SLEEP": 0.05,
    "MAXIMUM_SLEEP": 2.0,
    "DEFAULT_PAUSE": 0.1,
    "DEFAULT_DURATION": 0.1,
    "DEFAULT_INTERVAL": 0.05,
}


# ─── LOCALIZATION MAPPING ─────────────────────────────────────────────────────
MONTHS_ID = {
    "January": "Januari",
    "February": "Februari",
    "March": "Maret",
    "April": "April",
    "May": "Mei",
    "June": "Juni",
    "July": "Juli",
    "August": "Agustus",
    "September": "September",
    "October": "Oktober",
    "November": "November",
    "December": "Desember",
}


# ─── DEFAULT CONFIGURATION REGISTRY ──────────────────────────────────────────
DEFAULT_CONFIG = {
    **APPLICATION_PATHS,
    **FOLDER_PATHS,
    **CONTACT_INFO,
    "WAIT_TIME": WAIT_TIMES,
    "PYAUTOGUI": PYAUTOGUI_SETTINGS,
    "MONTHS_ID": MONTHS_ID,
}


# ─── PYAUTOGUI INITIALISATION ─────────────────────────────────────────────────
def setup_pyautogui_config() -> None:
    global _pyautogui_configured
    if _pyautogui_configured:
        return

    try:
        pyautogui.FAILSAFE = PYAUTOGUI_SETTINGS["FAILSAFE"]
        pyautogui.PAUSE = PYAUTOGUI_SETTINGS["PAUSE"]
        _pyautogui_configured = True
        logger.info("[SYSTEM] PYAUTOGUI CONFIGURED SUCCESSFULLY")
    except Exception as e:
        logger.error(f"[SYSTEM] FAILED TO CONFIGURE PYAUTOGUI: {e}")
        raise


# ─── TIMER UTILITIES ──────────────────────────────────────────────────────────
def wait_timer(base_time: float) -> None:
    time.sleep(base_time)


# ─── CONFIGURATION ACCESSORS ──────────────────────────────────────────────────
def get_config_value(key: str, default: Any = None) -> Any:
    config = DEFAULT_CONFIG
    keys = key.split(".")

    try:
        for k in keys:
            config = config[k]
        return config
    except (KeyError, TypeError):
        return default


def get_wait_time(time_key: str, default: float = 1.0) -> float:
    return WAIT_TIMES.get(time_key, default)


def get_pyautogui_setting(setting_name: str, default: Any = None) -> Any:
    return PYAUTOGUI_SETTINGS.get(setting_name, default)


def get_month_id(english_month: str, case: str = "as-is") -> str:
    indonesian_month = MONTHS_ID.get(english_month, english_month)
    if case == "upper":
        return indonesian_month.upper()
    elif case == "lower":
        return indonesian_month.lower()
    elif case == "title":
        return indonesian_month.title()
    return indonesian_month


# ─── PROCESS UTILITIES ────────────────────────────────────────────────────────
def scan_running_processes(target_names: list[str]) -> list[str]:
    found_processes: list[str] = []

    for proc in psutil.process_iter(["name"]):
        try:
            proc_name = proc.info.get("name") or ""
            if proc_name.lower() in [t.lower() for t in target_names]:
                found_processes.append(proc_name)
        except psutil.AccessDenied:
            logger.debug(f"[SYSTEM] ACCESS DENIED — SKIPPING PROCESS PID: {proc.pid}")
        except psutil.NoSuchProcess:
            logger.debug("[SYSTEM] PROCESS VANISHED DURING SCAN — SKIPPING")

    return found_processes


def is_process_running(process_name: str) -> bool:
    for proc in psutil.process_iter(["name"]):
        try:
            proc_info_name = proc.info.get("name") or ""
            if proc_info_name.lower() == process_name.lower():
                return True
        except psutil.AccessDenied:
            logger.debug(f"[SYSTEM] ACCESS DENIED — SKIPPING PROCESS PID: {proc.pid}")
        except psutil.NoSuchProcess:
            logger.debug("[SYSTEM] PROCESS VANISHED DURING SCAN — SKIPPING")

    return False
