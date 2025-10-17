# app/adapters/taskiq/broker.py
__all__ = (
    "broker",
)

import logging

from taskiq import TaskiqEvents, TaskiqState
from taskiq_aio_pika import AioPikaBroker

from core.config import settings, TaskiqConfig

logger = logging.getLogger(__name__)

broker = AioPikaBroker(
    url=settings.taskiq.url,
)


@broker.on_event(TaskiqEvents.WORKER_STARTUP)
async def on_event_startup(state: TaskiqState) -> None:
    logging.basicConfig(
        level=settings.logging.log_level_value,
        format=settings.taskiq.log_format,
        datefmt=settings.logging.log_date_format,
    )
    logger.info("broker startup complete, got state: %s", state)