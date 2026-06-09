import math
import pyautogui
import time
from pynput.keyboard import Controller, Key
from services.config import load_config, logger, wait_timer

CONFIG = load_config()
FIGURE_EIGHT_CONFIG = {"RADIUS_X": 250, "RADIUS_Y": 200, "TOTAL_DURATION": 5.0}
keyboard = Controller()


def accept_refresh():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] INSERTING LINE BREAKS IN COMPOSE BODY")
    for _ in range(3):
        pyautogui.press("enter")
        wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def action_paste():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("ctrl", "v")
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])


def backspace():
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    pyautogui.press("backspace")
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def blank_mail_space():
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    logger.info("[SYSTEM] INSERTING BLANK SPACING IN MAIL BODY")
    for _ in range(2):
        pyautogui.press("enter")
    pyautogui.press("backspace")
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def break_excel_link():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] CONVERTING EXCEL LINKS TO STATIC VALUES")
    for key in ["alt", "a", "k"]:
        pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("tab", presses=4)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("left")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def capture_table_as_bitmap():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] CONVERTING SELECTED TABLE TO BITMAP FORMAT")
    pyautogui.hotkey("ctrl", "a")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    for key in ["alt", "h", "c", "p"]:
        pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("tab")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("down")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])


def capture_table_as_picture():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] CONVERTING SELECTED TABLE TO PICTURE FORMAT")
    pyautogui.hotkey("ctrl", "a")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    for key in ["alt", "h", "c", "p"]:
        pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def capture_table_as_table():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] COPYING TABLE AS EDITABLE CELL FORMATTING")
    for _ in range(2):
        pyautogui.hotkey("ctrl", "a")
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    for key in ["alt", "h", "c", "c"]:
        pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])


def choose_file_attach():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] OPENING FILE ATTACHMENT DIALOG IN OUTLOOK")
    pyautogui.hotkey("alt", "n")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    for key in ["a", "f"]:
        pyautogui.press(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.press("tab", presses=6)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("space")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("backspace")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def click():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] PERFORMING SINGLE LEFT BUTTON MOUSE CLICK")
    pyautogui.click(button="left")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def close_unsave():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] CLOSING WORKBOOK AND DISCARDING CHANGES")
    pyautogui.hotkey("alt", "f4")
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.hotkey("tab")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["FIFTEEN_SECOND"])


def closing_tab():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] TERMINATING ACTIVE APPLICATION WINDOW")
    pyautogui.hotkey("alt", "f4")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def confirm():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] EXECUTING CONFIRMATION FOR OPERATION")
    pyautogui.press("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def confirm_file_attach():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] FINALISING FILE ATTACHMENT IN REPORT MAIL")
    pyautogui.press("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("tab", presses=4)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("space")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("enter")
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])


def convert_to_range():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] CONVERTING STRUCTURED OBJECT TO CELL RANGE")
    pyautogui.hotkey("alt")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("j", "t")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("g")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])


def creating_new_task():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] INITIATING NEW DOCUMENT OR TASK INSTANCE")
    pyautogui.hotkey("ctrl", "n")
    wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])


def define_center():
    screen_width, screen_height = pyautogui.size()
    return screen_width // 2, screen_height // 2


def entering_operation():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] PRESSING ENTER TO HANDLE OPERATION DIALOG")
    for _ in range(4):
        pyautogui.hotkey("enter")
        wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def escaping():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("esc")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def finish_outlook():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] DISPATCHING MESSAGE AND CLOSING OUTLOOK")
    pyautogui.hotkey("alt", "s")
    wait_timer(CONFIG["WAIT_TIME"]["TEN_SECOND"])
    pyautogui.hotkey("alt", "f4")
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])


def format_picture_width():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] FORMATTING IMAGE WIDTH TO TARGET SIZE")
    keyboard.press(Key.shift)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    keyboard.press(Key.left)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    keyboard.release(Key.shift)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    keyboard.release(Key.left)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("alt")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    for key in ["j", "p", "w"]:
        pyautogui.press(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.write("40")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    for _ in range(3):
        pyautogui.hotkey("enter")
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def handle_breaklink_process():
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    pyautogui.PAUSE = 0
    center_x, center_y = define_center()
    moving_process(
        center_x,
        center_y,
        FIGURE_EIGHT_CONFIG["RADIUS_X"],
        FIGURE_EIGHT_CONFIG["RADIUS_Y"],
        FIGURE_EIGHT_CONFIG["TOTAL_DURATION"],
    )

    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    pyautogui.press("alt")
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])

    moving_process(
        center_x,
        center_y,
        FIGURE_EIGHT_CONFIG["RADIUS_X"],
        FIGURE_EIGHT_CONFIG["RADIUS_Y"],
        FIGURE_EIGHT_CONFIG["TOTAL_DURATION"],
    )

    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def handle_move_copy_process():
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    pyautogui.PAUSE = 0
    center_x, center_y = define_center()
    moving_process(
        center_x,
        center_y,
        FIGURE_EIGHT_CONFIG["RADIUS_X"],
        FIGURE_EIGHT_CONFIG["RADIUS_Y"],
        FIGURE_EIGHT_CONFIG["TOTAL_DURATION"],
    )

    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    pyautogui.press("left")
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    pyautogui.press("right")
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])

    moving_process(
        center_x,
        center_y,
        FIGURE_EIGHT_CONFIG["RADIUS_X"],
        FIGURE_EIGHT_CONFIG["RADIUS_Y"],
        FIGURE_EIGHT_CONFIG["TOTAL_DURATION"],
    )

    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def handle_not_activated_office():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] SKIPPING OFFICE ACTIVATION PROMPT DIALOG")
    for _ in range(3):
        pyautogui.hotkey("esc")
        wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def handle_office():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] DISMISSING OFFICE APPLICATION DIALOGS")
    for _ in range(4):
        pyautogui.hotkey("esc")
        wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def handle_refresh_process():
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    logger.info("[SYSTEM] HANDLING EXCEL RECALCULATION PROCESS")
    move_cursor_figure_eight()
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    switch_to_first_cells()
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    move_cell_vertical()
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def input_clipboard_picture():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] INSERTING IMAGE CONTENT FROM CLIPBOARD")
    pyautogui.hotkey("ctrl", "v")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("right")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])


def input_dynamic_picture():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] PASTING IMAGE WITH PRESERVED SCALING DATA")
    pyautogui.hotkey("ctrl", "v")
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.hotkey("right")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("backspace")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def input_hyperlink():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] OPENING HYPERLINK DIALOG FOR URL INSERT")
    for key in ["alt", "n", "i"]:
        pyautogui.press(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def make_new_pivot_sheet():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] CREATING NEW WORKSHEET FOR PIVOT TABLE")
    for key in ["alt", "n", "v", "t"]:
        pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def maximize_app_window():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] EXPANDING ACTIVE WINDOW TO FULL SCREEN")
    pyautogui.hotkey("win", "up")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def minimize_outlook():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("win", "m")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def minimize_text():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] REDUCING FONT SIZE OF SELECTED CELL TEXT")
    for _ in range(2):
        for key in ["alt", "h", "f", "k"]:
            pyautogui.hotkey(key)
            wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def move_cell_horizontal():
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    logger.info("[DATA] MOVING CELL HORIZONTALLY TO KEEP ACTIVE")
    for _ in range(2):
        pyautogui.hotkey("ctrl", "right")
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    for _ in range(2):
        pyautogui.hotkey("ctrl", "left")
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def move_cell_vertical():
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    logger.info("[DATA] NAVIGATING CELLS VERTICALLY TO STAY ACTIVE")
    for _ in range(3):
        pyautogui.hotkey("ctrl", "down")
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    for _ in range(5):
        pyautogui.hotkey("ctrl", "up")
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def move_cursor_figure_eight():
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    pyautogui.PAUSE = 0
    center_x, center_y = define_center()

    moving_process(
        center_x,
        center_y,
        FIGURE_EIGHT_CONFIG["RADIUS_X"],
        FIGURE_EIGHT_CONFIG["RADIUS_Y"],
        FIGURE_EIGHT_CONFIG["TOTAL_DURATION"],
    )

    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    pyautogui.click()
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])

    moving_process(
        center_x,
        center_y,
        FIGURE_EIGHT_CONFIG["RADIUS_X"],
        FIGURE_EIGHT_CONFIG["RADIUS_Y"],
        FIGURE_EIGHT_CONFIG["TOTAL_DURATION"],
    )

    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def move_or_copy_as_newbook():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] DUPLICATING WORKSHEET INTO NEW WORKBOOK")
    pyautogui.hotkey("tab")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("space")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("tab", presses=3)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("space")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("up", presses=5)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("tab", presses=3)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def move_or_copy_menu():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] ACCESSING MOVE OR COPY RELOCATION DIALOG")
    for key in ["alt", "e", "m"]:
        pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def moving_process(center_x, center_y, radius_x, radius_y, total_duration):
    start_time = time.perf_counter()
    while True:
        elapsed = time.perf_counter() - start_time
        if elapsed >= total_duration:
            return

        progress = (elapsed / total_duration) * (2 * math.pi)
        x = center_x + radius_x * math.sin(progress)
        y = center_y + radius_y * math.sin(2 * progress) / 2
        pyautogui.moveTo(x, y, duration=0)


def paste_value_as_value():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] PASTING CLIPBOARD CONTENT AS PLAIN VALUES")
    for key in ["alt", "h", "v", "v"]:
        pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])


def refresh_excel_data():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] REFRESHING ALL DATA CONNECTIONS IN EXCEL")
    for key in ["alt", "a", "r", "a"]:
        pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def save_as_in():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] ACCESSING SAVE AS DIALOG TO TARGET DIR")
    pyautogui.hotkey("f12")
    wait_timer(CONFIG["WAIT_TIME"]["TEN_SECOND"])
    pyautogui.press("tab", presses=10)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("space")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def save_as_name():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] POSITIONING CURSOR IN SAVE AS FILENAME")
    pyautogui.press("tab", presses=6)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("backspace")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def save_excel():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("ctrl", "s")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def save_file():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] PERSISTING CURRENT DOCUMENT TO STORAGE")
    pyautogui.hotkey("ctrl", "s")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def save_new_book():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] SAVING NEW WORKBOOK TO SPECIFIED LOCATION")
    pyautogui.hotkey("ctrl", "s")
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.press("tab", presses=2)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.press("tab", presses=11)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("space")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("backspace")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def save_new_copy():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] SAVING FILE WITH NEW NAME IN TARGET DIR")
    pyautogui.hotkey("ctrl", "s")
    wait_timer(CONFIG["WAIT_TIME"]["TWENTY_SECOND"])
    pyautogui.press("tab", presses=10)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    for action in [("press", "space"), ("press", "backspace")]:
        getattr(pyautogui, action[0])(action[1])
        wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])


def scroller_page(scroll_amount: int = 500) -> None:
    if not isinstance(scroll_amount, int):
        raise TypeError("scroll_amount must be integer")

    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.PAUSE = 0
    pyautogui.scroll(scroll_amount)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.scroll(-scroll_amount)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def select_header_content():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    logger.info("[SYSTEM] SELECTING HEADER SECTION CONTENT RANGE")
    for _ in range(5):
        keyboard.press(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.up)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.up)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def select_hyperlink():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] HIGHLIGHTING HYPERLINK TEXT IN DOCUMENT")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    keyboard.press(Key.shift)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    keyboard.press(Key.up)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    keyboard.release(Key.shift)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    keyboard.release(Key.up)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def select_sheet_down():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] EXTENDING WORKSHEET SELECTION DOWNWARD")
    for _ in range(15):
        keyboard.press(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.page_down)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.page_down)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def select_sheet_half_down():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] SELECTING PARTIAL WORKSHEET RANGE DOWN")
    for _ in range(5):
        keyboard.press(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.page_down)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.page_down)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def select_sheet_half_up():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] SELECTING PARTIAL WORKSHEET RANGE UP")
    for _ in range(5):
        keyboard.press(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.page_up)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.page_up)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def select_sheet_order_in():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] SELECTING WORKSHEETS FOR REPORT ORDER")
    for _ in range(2):
        keyboard.press(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.page_down)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.page_down)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def select_sheet_performance():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] SELECTING ALL PERFORMANCE SHEET RANGES")
    for _ in range(55):
        keyboard.press(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.page_down)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.page_down)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])


def select_sheet_up():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] EXTENDING WORKSHEET SELECTION UPWARD")
    for _ in range(10):
        keyboard.press(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.press(Key.page_up)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.page_up)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.shift)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
        keyboard.release(Key.ctrl)
        wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def send_outlook():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("alt", "s")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def set_new_book_name():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] CLEARING FILENAME AND PREPARING FOR INPUT")
    pyautogui.press("tab", presses=6)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("space")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("backspace")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def set_new_pivot_sheet():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[DATA] CONFIGURING PIVOT TABLE LAYOUT AND DESIGN")
    for _ in range(2):
        for key in ["alt", "j", "t", "l"]:
            pyautogui.hotkey(key)
            wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("tab")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("space")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("tab")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("up", presses=4)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.hotkey("enter")
    wait_timer(CONFIG["WAIT_TIME"]["FIVE_SECOND"])
    pyautogui.hotkey("esc")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def set_text_right():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] APPLYING RIGHT ALIGNMENT TO CELL CONTENT")
    for key in ["alt", "h", "a", "r"]:
        pyautogui.press(key) if key in ("alt",) else pyautogui.hotkey(key)
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    for _ in range(2):
        pyautogui.press("right")
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def switch_to_first_cells():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] NAVIGATING TO FIRST CELL AT TOP LEFT")
    for _ in range(5):
        pyautogui.hotkey("ctrl", "up")
    for _ in range(5):
        pyautogui.hotkey("ctrl", "left")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def switch_to_first_sheet():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] TRANSITIONING NAVIGATION TO FIRST SHEET")
    for _ in range(15):
        pyautogui.hotkey("ctrl", "pgup")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def switch_to_first_sheet_performance():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] TRANSITIONING TO FIRST PERFORMANCE SHEET")
    for _ in range(50):
        pyautogui.hotkey("ctrl", "pgup")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def switch_to_last_sheet():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] TRANSITIONING NAVIGATION TO LAST SHEET")
    for _ in range(15):
        pyautogui.hotkey("ctrl", "pagedown")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def switch_to_left_sheet():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] SWITCHING NAVIGATION TO LEFT WORKSHEET")
    pyautogui.hotkey("ctrl", "pgup")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def switch_to_right_sheet():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] SWITCHING NAVIGATION TO RIGHT WORKSHEET")
    pyautogui.hotkey("ctrl", "pagedown")
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])


def switch_to_table_cells():
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    logger.info("[SYSTEM] NAVIGATING TO TABLE SUMMARY CELL RANGE")
    pyautogui.press("down", presses=3)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
    pyautogui.press("right", presses=3)
    wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])
