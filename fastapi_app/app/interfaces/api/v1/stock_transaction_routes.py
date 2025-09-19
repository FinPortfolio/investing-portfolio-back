# app/interfaces/api/v1/stock_transaction_routes.py
from fastapi import APIRouter

from app.adapters.deps import StockTranServiceDep
from app.interfaces.schemas import StockTranPublic
from core.config import settings

stock_transaction_router = APIRouter(
    prefix=settings.api.v1.stock_transactions,
    tags=["Stock Transactions"],
)


@stock_transaction_router.get("/", response_model=list[StockTranPublic])
async def read_stock_transactions(service: StockTranServiceDep):
    stock_trans = await service.get_all_stock_transactions()
    return [StockTranPublic.from_entity(stock_tran) for stock_tran in stock_trans]