# app/interfaces/api/v1/stock_transaction_routes.py
from fastapi import APIRouter, HTTPException, Response, status

from app.adapters.deps import StockTranServiceDep
from app.interfaces.schemas import StockTranCreate, StockTranPublic
from core.config import settings

stock_transaction_router = APIRouter(
    prefix=settings.api.v1.stock_transactions,
    tags=["Stock Transactions"],
)


@stock_transaction_router.get("/", response_model=list[StockTranPublic])
async def read_stock_transactions(service: StockTranServiceDep):
    stock_trans = await service.get_all_stock_transactions()
    return [StockTranPublic.from_entity(stock_tran) for stock_tran in stock_trans]


@stock_transaction_router.post("/", response_model=StockTranPublic, status_code=status.HTTP_201_CREATED)
async def create_stock_transaction(
    stock_tran: StockTranCreate,
    service: StockTranServiceDep
):
    # stock = await service.add_stock(stock.to_entity())
    stock_tran_entity = await service.add_stock_tran(stock_tran.model_dump())
    return StockTranPublic.from_entity(stock_tran_entity)