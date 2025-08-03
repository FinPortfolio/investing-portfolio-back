# app/adapters/deps.py
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from app.adapters.db.session import get_session
from app.adapters.db.repositories.stock_repository_impl import SQLAlchemyStockRepository
from app.application.services.stock_service import StockService

SessionDep = Annotated[Session, Depends(get_session)]

def get_stock_service(session: SessionDep) -> StockService:
    repo = SQLAlchemyStockRepository(session)
    return StockService(repo)

StockServiceDep = Annotated[StockService, Depends(get_stock_service)]
