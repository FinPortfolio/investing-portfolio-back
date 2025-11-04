# app/adapters/taskiq/tasks/fetch_stock_info_task.py
import logging

from taskiq import TaskiqDepends, Context
from app.adapters.external.alphavantage_client import AlphaVantageClient
# from app.adapters.db.models import StockRegistry, StockDetail
# from app.adapters.db.session import get_session
from app.adapters.taskiq.broker import broker
# from sqlalchemy import update

logger = logging.getLogger(__name__)


@broker.task
async def fetch_stock_info_task(registry_id: int, provider: str, ticker: str):
    client = AlphaVantageClient()
    data = await client.get_stock_overview(ticker)
    logger.info("____________registry_id: %s", registry_id)
    logger.info("____________provider: %s", provider)
    logger.info("____________data: %s", data)
    # async with get_session() as session:
    #     detail = StockDetail(
    #         registry_id=registry_id,
    #         ticker=ticker,
    #         provider=provider,
    #         data=data,
    #     )
    #     session.add(detail)
    #     await session.execute(
    #         update(StockRegistry)
    #         .where(StockRegistry.id == registry_id)
    #         .values(has_detailed_info=True)
    #     )
    #     await session.commit()
