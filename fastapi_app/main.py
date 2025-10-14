from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.interfaces.api.v1 import router_v1
from core.config import settings
from app.adapters.taskiq import broker
from app.adapters.taskiq.tasks import taskiq_send_welcome_email
from app.adapters.db import pg_db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await broker.startup()
    yield
    # shutdown
    await pg_db_manager.dispose()
    await broker.shutdown()


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
    await taskiq_send_welcome_email.kiq()
    return {"message": "Everything is OK!!!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
