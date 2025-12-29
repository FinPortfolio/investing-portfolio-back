__all__ = (
    "router_v1",
)

from fastapi import APIRouter

from core.config import settings

from .stock_routes import stock_router
from .stock_transaction_routes import stock_transaction_router

router_v1 = APIRouter(
    prefix=settings.api.v1.prefix,
)

router_v1.include_router(stock_router)

router_v1.include_router(stock_transaction_router)