# app/adapters/deps.py
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db import pg_db_manager
from app.adapters.db.repositories import (
    SQLAStockRepository,
    SQLAStockTranRepository,
)
from app.application.services import (
    StockService,
    StockTranService,
)

SessionDep = Annotated[AsyncSession, Depends(pg_db_manager.session_getter)]


async def get_stock_service(session: SessionDep) -> StockService:
    repo = SQLAStockRepository(session)
    return StockService(repo)


StockServiceDep = Annotated[StockService, Depends(get_stock_service)]


async def get_stock_transaction_service(session: SessionDep) -> StockTranService:
    tran_repo = SQLAStockTranRepository(session)
    stock_repo = SQLAStockRepository(session)
    return StockTranService(tran_repo, stock_repo)


StockTranServiceDep = Annotated[StockTranService, Depends(get_stock_transaction_service)]
