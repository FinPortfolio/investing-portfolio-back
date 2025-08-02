from fastapi import APIRouter, Depends

from app.interfaces.schemas.stock_schema import StockPublic
from app.interfaces.deps import get_stock_service

router = APIRouter()


@router.get("/stocks/{stock_id}", response_model=StockPublic)
def read_user(stock_id: int, service = Depends(get_stock_service)):
    return service.get_stock(stock_id)
