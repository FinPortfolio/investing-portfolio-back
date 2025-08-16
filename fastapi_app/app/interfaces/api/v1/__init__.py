__all__ = (
    "router",
)

from fastapi import APIRouter

from core.config import settings

from .stock_routes import router as stock_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    prefix=settings.api.v1.stocks,
    router=stock_router,
)
