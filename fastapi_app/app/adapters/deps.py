# app/adapters/deps.py
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db import pg_db_manager
from app.adapters.db.repositories import (
    SQLAlchemyStockRepository,
    SQLAStockTranRepository,
)
from app.application.services import (
    StockService,
    StockTranService,
)

SessionDep = Annotated[AsyncSession, Depends(pg_db_manager.session_getter)]


async def get_stock_service(session: SessionDep) -> StockService:
    repo = SQLAlchemyStockRepository(session)
    return StockService(repo)


StockServiceDep = Annotated[StockService, Depends(get_stock_service)]


async def get_stock_transaction_service(session: SessionDep) -> StockTranService:
    repo = SQLAStockTranRepository(session)
    return StockTranService(repo)


StockTranServiceDep = Annotated[StockTranService, Depends(get_stock_transaction_service)]