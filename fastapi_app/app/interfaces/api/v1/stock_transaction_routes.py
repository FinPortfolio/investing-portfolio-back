# app/interfaces/api/v1/stock_transaction_routes.py
from fastapi import APIRouter

from app.adapters.deps import StockTransServiceDep
from core.config import settings

stock_transaction_router = APIRouter(
    prefix=settings.api.v1.stock_transactions,
    tags=["Stock Transactions"],
)


async def read_stock_transactions(service: StockTransServiceDep):
    stock_trans = await service.get_all_stock_transactions()
    return [StockTransactionPublic.from_entity(stock_tran) for stock_tran in stock_trans]