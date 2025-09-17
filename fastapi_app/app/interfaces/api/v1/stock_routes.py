# app/interfaces/api/v1/stock_routes.py
from fastapi import APIRouter, HTTPException, Response, status

from app.application.exceptions import StockNotFoundError
from app.interfaces.schemas import (
    StockCreate,
    StockPublic,
    StockFullUpdate,
    StockPartialUpdate,
)
from app.adapters.deps import StockServiceDep


router = APIRouter(
    tags=["Stocks"],
)


@router.get("/", response_model=list[StockPublic])
async def read_stocks(
    service: StockServiceDep,
):
    stocks = await service.get_all_stocks()
    return [StockPublic.from_entity(stock) for stock in stocks]


@router.post("/", response_model=StockPublic, status_code=status.HTTP_201_CREATED)
async def create_stock(
    stock: StockCreate,
    service: StockServiceDep
):
    # stock = await service.add_stock(stock.to_entity())
    stock_entity = await service.add_stock(stock.model_dump())
    return StockPublic.from_entity(stock_entity)


@router.get("/{stock_id}/", response_model=StockPublic)
async def read_stock(
    stock_id: int,
    service: StockServiceDep
):
    try:
        stock_entity = await service.get_stock(stock_id)
    except StockNotFoundError:
        raise HTTPException(status_code=404, detail="Stock not found")
    return StockPublic.from_entity(stock_entity)


@router.put("/{stock_id}", response_model=StockPublic)
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
    except StockNotFoundError:
        raise HTTPException(status_code=404, detail="Stock not found")
    return StockPublic.from_entity(stock_entity)


@router.patch("/{stock_id}", response_model=StockPublic)
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
    except StockNotFoundError:
        raise HTTPException(status_code=404, detail="Stock not found")
    return StockPublic.from_entity(stock_entity)


@router.delete("/{stock_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_stock(
    stock_id: int,
    service: StockServiceDep
):
    try:
        await service.delete_stock(
            stock_id=stock_id,
        )
    except StockNotFoundError:
        raise HTTPException(status_code=404, detail="Stock not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
