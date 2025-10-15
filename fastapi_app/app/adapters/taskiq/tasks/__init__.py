__all__ = (
    "taskiq_send_welcome_email",
)

import logging
import sys

from core.config import settings
from .email_tasks import taskiq_send_welcome_email

if sys.argv[0] == "worker":
    logging.basicConfig(
        level=settings.logging.log_level_value,
        format=settings.logging.log_format,
    )