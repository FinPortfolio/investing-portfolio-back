# app/interfaces/api/v1/stock_transaction_routes.py
from fastapi import APIRouter, HTTPException, Response, status

from app.adapters.deps import StockTranServiceDep
from app.application.exceptions import StockNotFoundError, StockTranNotFoundError
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
    try:
        stock_tran_entity = await service.add_stock_tran(stock_tran.model_dump())
    except StockNotFoundError:
        raise HTTPException(status_code=422, detail="Stock with this ticker not found")
    return StockTranPublic.from_entity(stock_tran_entity)


@stock_transaction_router.get("/{transaction_id}/", response_model=StockTranPublic)
async def read_stock(
    transaction_id: int,
    service: StockTranServiceDep
):
    try:
        stock_tran_entity = await service.get_stock_tran(transaction_id)
    except StockTranNotFoundError:
        raise HTTPException(status_code=404, detail="Stock Transaction not found")
    return StockTranPublic.from_entity(stock_tran_entity)


@stock_transaction_router.delete("/{transaction_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_stock(
    transaction_id: int,
    service: StockTranServiceDep
):
    try:
        await service.delete_stock_tran(
            transaction_id=transaction_id,
        )
    except StockTranNotFoundError:
        raise HTTPException(status_code=404, detail="Stock Transaction not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
