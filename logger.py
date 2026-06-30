"""
logger.py
Logging utilities for SignalDecoder
"""

import logging
from pathlib import Path


class SignalLogger:
    """
    Logger wrapper for SignalDecoder.
    """

    def __init__(
        self,
        log_file="signaldecoder.log",
        level=logging.INFO
    ):
        self.log_file = Path(log_file)

        self.logger = logging.getLogger("SignalDecoder")
        self.logger.setLevel(level)

        # Prevent duplicate handlers
        if not self.logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                self.log_file,
                encoding="utf-8"
            )
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":

    logger = SignalLogger()

    logger.info("SignalDecoder started.")
    logger.debug("Debug message.")
    logger.warning("Warning message.")
    logger.error("Example error.")
    logger.critical("Critical message.")
