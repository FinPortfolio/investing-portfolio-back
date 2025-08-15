__all__ = (
    "router",
)

from fastapi import APIRouter

from .stock_routes import router as stock_router

router = APIRouter(
    prefix="/v1"
)

router.include_router(router=stock_router, prefix="/stocks")
