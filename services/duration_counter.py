import time
from services.config import logger


start_time = None
end_time = None
timer_active = False


def start_timer():
    global start_time, timer_active
    start_time = time.time()
    timer_active = True
    logger.info("Timer Started")
    return start_time


def stop_timer():
    global end_time, timer_active
    if not timer_active:
        logger.error("Timer Not Started")
        return None

    end_time = time.time()
    timer_active = False
    logger.info("Timer Stopped")
    return end_time


def get_duration(format_output=True):
    global start_time, end_time

    if start_time is None:
        logger.error("Duration Unavailable - Timer Not Started")
        return None

    execution_seconds = (time.time() if end_time is None else end_time) - start_time

    if format_output:
        hours, remainder = divmod(execution_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

    return execution_seconds


def log_execution_time(process_name=None):
    execution_time = get_duration()
    suffix = f" [{process_name.upper()}]" if process_name else ""
    log_message = f"Execution Time{suffix}: {execution_time}"
    logger.info(log_message)
    return log_message


def reset_timer():
    global start_time, end_time, timer_active
    start_time = None
    end_time = None
    timer_active = False
    logger.debug("Timer Reset")


def is_timer_active():
    return timer_active


class ExecutionTimer:
    def __init__(self, process_name=None):
        self.process_name = process_name

    def __enter__(self):
        start_timer()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        stop_timer()
        log_execution_time(self.process_name)
        return False
