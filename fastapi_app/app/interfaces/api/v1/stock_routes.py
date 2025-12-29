# app/interfaces/api/v1/stock_routes.py
from fastapi import APIRouter, HTTPException, Response, status

from app.adapters.exceptions import StockNotFoundError
from app.interfaces.schemas import (
    StockCreate,
    StockPublic,
    StockFullUpdate,
    StockPartialUpdate,
)
from app.adapters.deps import StockServiceDep
from core.config import settings

stock_router = APIRouter(
    prefix=settings.api.v1.stocks,
    tags=["Stocks"],
)


@stock_router.get("/", response_model=list[StockPublic])
async def read_stocks(
    service: StockServiceDep,
):
    stocks = await service.get_all_stocks()
    return [StockPublic.from_entity(stock) for stock in stocks]


@stock_router.post("/", response_model=StockPublic, status_code=status.HTTP_201_CREATED)
async def create_stock(
    stock: StockCreate,
    service: StockServiceDep
):
    # stock = await service.add_stock(stock.to_entity())
    stock_entity = await service.add_stock(stock.model_dump())
    return StockPublic.from_entity(stock_entity)


@stock_router.get("/{stock_id}/", response_model=StockPublic)
async def read_stock(
    stock_id: int,
    service: StockServiceDep
):
    try:
        stock_entity = await service.get_stock(stock_id)
    except StockNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return StockPublic.from_entity(stock_entity)


@stock_router.put("/{stock_id}", response_model=StockPublic)
async def full_update_stock(
    stock_id: int,
    stock: StockFullUpdate,
    service: StockServiceDep
):
    try:
        stock_entity = await service.update_stock(
            stock_id=stock_id,
            stock=stock.model_dump(),
        )
    except StockNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return StockPublic.from_entity(stock_entity)


@stock_router.patch("/{stock_id}", response_model=StockPublic)
async def partial_update_stock(
    stock_id: int,
    stock: StockPartialUpdate,
    service: StockServiceDep
):
    try:
        stock_entity = await service.update_stock(
            stock_id=stock_id,
            stock=stock.model_dump(exclude_unset=True),
        )
    except StockNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return StockPublic.from_entity(stock_entity)


@stock_router.delete("/{stock_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_stock(
    stock_id: int,
    service: StockServiceDep
):
    try:
        await service.delete_stock(
            stock_id=stock_id,
        )
    except StockNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
