from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.interfaces.api.v1 import router as router_v1
from core.config import settings
from app.adapters.db import pg_db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    pg_db_manager.engine.dispose()


main_app = FastAPI(
    lifespan=lifespan,
    title="Investing Portfolio API",
)

main_app.include_router(
    router=router_v1,
    prefix=settings.api.prefix
)


@main_app.get("/")
async def read_stocks():
    return {"message": "Everything is OK"}


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
