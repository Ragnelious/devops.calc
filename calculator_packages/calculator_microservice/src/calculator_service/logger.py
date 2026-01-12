import atexit
import logging
import os
import sys
from functools import lru_cache
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Dict, Optional, Union

DEFAULT_LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
DEFAULT_LOG_DIR = os.getenv("LOG_DIR", "logs")
DEFAULT_LOG_FILE = "calculator_service.log"


@lru_cache(maxsize=None)
def get_logger(
    name: str,
    level: Optional[str] = None,
    log_dir: Optional[Union[str, Path]] = None,
) -> logging.Logger:
    """
    Create or retrieve a configured logger instance.

    :param name: Logger name
    :param level: Log level (INFO, DEBUG, etc.)
    :param log_dir: Directory where log files will be stored
    :return: Configured logger
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level or DEFAULT_LOG_LEVEL)

    # =====================
    # Formatter
    # =====================
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    )

    # =====================
    # Console handler
    # =====================
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # =====================
    # File handler (Rotating)
    # =====================
    log_directory = Path(log_dir or DEFAULT_LOG_DIR)
    log_directory.mkdir(parents=True, exist_ok=True)

    file_handler = RotatingFileHandler(
        log_directory / DEFAULT_LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5,
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


def _shutdown_logging():
    """
    Ensure all logging handlers are flushed and closed on exit.
    """
    logging.shutdown()


# =====================
# Register cleanup
# =====================
atexit.register(_shutdown_logging)
