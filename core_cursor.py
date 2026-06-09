from __future__ import annotations

import signal
import threading
from dataclasses import dataclass, field
from datetime import datetime
from types import FrameType
from typing import List

from pynput import keyboard, mouse

from services.config import load_config, logger, wait_timer


@dataclass
class ClickEntry:
    index: int
    x: int
    y: int

    timestamp: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    )

    def __str__(self) -> str:
        return (
            f"CLICK DETECTED AT POSITION -> "
            f"X: {self.x:>6}, Y: {self.y:>6}  "
            f"| #{self.index:>4}  | {self.timestamp}"
        )


class ClickRecorder:
    DIVIDER = "▬" * 41

    def __init__(self) -> None:
        self.clicks: List[ClickEntry] = []
        self._config = load_config()

        self.cursor_listener: mouse.Listener | None = None
        self.keyboard_listener: keyboard.Listener | None = None

        self.stop_key_press = threading.Event()

    def print_banner(self) -> None:
        print(self.DIVIDER)
        print("PRESS ENTER TO STOP RECORDING.")
        print(self.DIVIDER)

    def clicked(
        self,
        x: int,
        y: int,
        button: mouse.Button,
        pressed: bool,
    ) -> None:
        if self.stop_key_press.is_set():
            return

        if button == mouse.Button.left and pressed:
            entry = ClickEntry(
                index=len(self.clicks) + 1,
                x=x,
                y=y,
            )

            self.clicks.append(entry)
            logger.info(str(entry))

    def stop_key(
        self,
        key: keyboard.Key | keyboard.KeyCode | None,
    ) -> None:
        if key == keyboard.Key.enter:
            logger.warning("STOP RECORDING WITH ENTER")
            self.stop()

    def start(self) -> None:
        self.print_banner()
        logger.info("LISTENER ACTIVE")

        try:
            self.cursor_listener = mouse.Listener(
                on_click=self.clicked,
            )

            self.keyboard_listener = keyboard.Listener(
                on_press=self.stop_key,
            )

            self.cursor_listener.start()
            self.keyboard_listener.start()

            self.stop_key_press.wait()

        except Exception as exc:
            logger.error(f"LISTENER ERROR : {exc}")

        finally:
            self.cleanup_listeners()

    def stop(self) -> None:
        self.stop_key_press.set()

    def cleanup_listeners(self) -> None:
        if self.cursor_listener is not None and self.cursor_listener.is_alive():
            self.cursor_listener.stop()

        if self.keyboard_listener is not None and self.keyboard_listener.is_alive():
            self.keyboard_listener.stop()

    def print_summary(self) -> None:
        wait_time = self._config["WAIT_TIME"]

        logger.info(f"RECORD LIST : {len(self.clicks)}")

        wait_timer(wait_time["HALF_SECOND"])

        if not self.clicks:
            logger.warning("NO RECORD FOUND.")
            return

        for entry in self.clicks:
            logger.debug(
                f"#{entry.index:>4} -> "
                f"X: {entry.x:>6}, "
                f"Y: {entry.y:>6}  "
                f"| {entry.timestamp}"
            )

            wait_timer(wait_time["TENTH_SECOND"])

    def get_coordinates(self) -> list[tuple[int, int]]:
        return [(entry.x, entry.y) for entry in self.clicks]


def main() -> None:
    recorder = ClickRecorder()

    def handling_interruption(
        signum: int,
        frame: FrameType | None,
    ) -> None:
        logger.warning("STOP RECORDING WITH CTRL + C")
        recorder.stop()

    signal.signal(
        signal.SIGINT,
        handling_interruption,
    )

    try:
        recorder.start()

    except Exception as exc:
        logger.critical(f"EXCEPTION : {exc}")

    finally:
        recorder.print_summary()
        logger.info("SESSION END")


if __name__ == "__main__":
    main()
