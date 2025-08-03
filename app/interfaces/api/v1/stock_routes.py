# app/adapters/api/v1/stock_routes.py
from fastapi import APIRouter, HTTPException

from app.application.exceptions import StockNotFoundError
from app.interfaces.schemas.stock_schema import StockCreate, StockPublic
from app.adapters.deps import StockServiceDep

router = APIRouter()


@router.get("/stocks/{stock_id}", response_model=StockPublic)
def read_stock(
        stock_id: int,
        service: StockServiceDep
):
    try:
        stock = service.get_stock(stock_id)
    except StockNotFoundError:
        raise HTTPException(status_code=404, detail="Stock not found")
    return StockPublic.from_entity(stock)

@router.post("/stocks", response_model=StockPublic)
def create_stock(
        stock: StockCreate,
        service: StockServiceDep
):
    stock = service.add_stock(stock.to_entity())
    return StockPublic.from_entity(stock)
