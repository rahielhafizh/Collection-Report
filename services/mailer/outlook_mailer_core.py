from __future__ import annotations
import pyautogui
from dataclasses import dataclass
from services.check.capslock_checker import capslock_checking
from services.check.chrome_checker import open_outlook
from services.config import load_config, logger, wait_timer
from typing import List, Union
from general_task import (
    backspace,
    blank_mail_space,
    choose_file_attach,
    confirm,
    confirm_file_attach,
    creating_new_task,
    format_picture_width,
    input_clipboard_picture,
    maximize_app_window,
    minimize_outlook,
    send_outlook,
)


CONFIG = load_config()


@dataclass(frozen=True)
class MailerProfile:
    name: str
    submission_config_key: str
    format_picture_after_paste: bool = False
    outlook_ready_wait_key: str = "TEN_SECOND"


class OutlookMailer:
    def __init__(self, profile: MailerProfile) -> None:
        self._profile = profile

    def send(
        self,
        to: Union[str, List[str]],
        cc: Union[str, List[str]],
        subject: str,
        body: str,
        footer: str,
    ) -> None:
        logger.info(f"[MAILER] INITIATING : {self._profile.name}")

        try:
            self.initialize_outlook_session()
            creating_new_task()
            wait_timer(CONFIG["WAIT_TIME"]["TWO_SECOND"])
            self.populate_recipient_field(self.normalize_address(to, "TO"))
            wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
            self.navigate_to_next_field()
            wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
            self.populate_recipient_field(self.normalize_address(cc, "CC"))
            wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
            self.navigate_to_next_field()
            wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
            self.populate_email_subject(subject)
            wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
            self.attach_submission_document()
            wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
            self.compose_email_body(body, footer)
            wait_timer(CONFIG["WAIT_TIME"]["TENTH_SECOND"])
            self.dispatch_mail()
            logger.info(f"[MAILER] COMPLETED : {self._profile.name}")

        except Exception as exc:
            logger.error(f"[MAILER] FAILED : {self._profile.name} — {exc}")
            raise

    def initialize_outlook_session(self) -> None:
        if not open_outlook():
            raise RuntimeError("Failed to activate or launch Outlook.")
        wait_timer(CONFIG["WAIT_TIME"][self._profile.outlook_ready_wait_key])
        maximize_app_window()
        capslock_checking()
        wait_timer(CONFIG["WAIT_TIME"]["ONE_SECOND"])

    def populate_recipient_field(self, addresses: List[str]) -> None:
        for idx, address in enumerate(addresses):
            pyautogui.write(address)
            confirm()
            if idx < len(addresses) - 1:
                wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])

    def navigate_to_next_field(self) -> None:
        pyautogui.press("tab")
        wait_timer(CONFIG["WAIT_TIME"]["HALF_SECOND"])

    def populate_email_subject(self, subject: str) -> None:
        pyautogui.write(subject)
        self.navigate_to_next_field()

    def attach_submission_document(self) -> None:
        choose_file_attach()
        pyautogui.write(CONFIG[self._profile.submission_config_key])
        confirm_file_attach()

    def compose_email_body(self, body: str, footer: str) -> None:
        pyautogui.write(body)
        blank_mail_space()
        input_clipboard_picture()

        if self._profile.format_picture_after_paste:
            backspace()
            format_picture_width()

        pyautogui.write(footer)

    def dispatch_mail(self) -> None:
        send_outlook()
        wait_timer(CONFIG["WAIT_TIME"]["THREE_SECOND"])
        minimize_outlook()

    @staticmethod
    def normalize_address(value: Union[str, List[str]], field_name: str) -> List[str]:
        if isinstance(value, str):
            return [value]
        if isinstance(value, list):
            return value
        raise TypeError(f"{field_name} must be str or list, got {type(value).__name__}")
