"""Common shared code for tasks."""

import os
from pathlib import Path

from robocorp import log


ARTIFACTS_DIR = os.getenv("ROBOT_ARTIFACTS", "output")
ROBOT_ROOT = os.getenv("ROBOT_ROOT", Path(__file__).parent.parent)
DEVDATA = Path(ROBOT_ROOT) / "devdata"


def setup_log() -> None:
    """Tries to use the LOG_LEVEL text asset or environment variable
    to set the log level. If the value is not valid, the default is
    "info". The environment variable will override the asset value.
    """
    if os.getenv("DEV_ENVIRONMENT"):
        log_level = os.getenv("LOG_LEVEL", "debug")
    else:
        log_level = os.getenv("LOG_LEVEL", "info")
        log.add_sensitive_variable_name_pattern(".*")

    try:
        log_level = log.FilterLogLevel(log_level)
    except ValueError:
        log_level = log.FilterLogLevel.INFO
    log.setup_log(output_log_level=log_level)
