# app/adapters/deps.py
from typing import Annotated
from fastapi import Depends
# from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

# from app.adapters.db.session import get_session
from app.adapters.db import db_manager
from app.adapters.db.repositories import SQLAlchemyStockRepository
from app.application.services import StockService

SessionDep = Annotated[AsyncSession, Depends(db_manager.scoped_session_dependency)]


async def get_stock_service(session: SessionDep) -> StockService:
    repo = SQLAlchemyStockRepository(session)
    return StockService(repo)


StockServiceDep = Annotated[StockService, Depends(get_stock_service)]
