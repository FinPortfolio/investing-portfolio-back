from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.adapters.db import db_manager
from app.adapters.db.models import Base
from app.interfaces.api.v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Investing Portfolio API",
)

app.include_router(router=router_v1, prefix="/api/v1")
