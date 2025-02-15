import sys
from logging import Formatter, Logger, StreamHandler, getLogger
import logging


LOGGER_NAME = "what-ya-wanna-read"
LOG_LEVEL = "DEBUG"

DEFAULT_LOGGERS = [
    LOGGER_NAME,
    "uvicorn.error",
    "uvicorn.access",
]

def configure_logger():
    logger = getLogger(LOGGER_NAME)
    std_out_handler = StreamHandler(
        stream=sys.stderr,
    )
    formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    std_out_handler.setFormatter(formatter)
    std_out_handler.setFormatter(formatter)
    logger.addHandler(std_out_handler)
    logger.setLevel(LOG_LEVEL)
    for name, logger in logging.root.manager.loggerDict.items():
        if not isinstance(logger, logging.Logger):
            continue
        if name in DEFAULT_LOGGERS:
            logger.handlers.clear()
            logger.disabled = False
            logger.addHandler(std_out_handler)
            logger.setLevel(LOG_LEVEL)
        else:
            logger.handlers.clear()
            logger.disabled = True


def get_logger() -> Logger:
    return getLogger(LOGGER_NAME)
