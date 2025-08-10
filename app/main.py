from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.interfaces.api.v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Investing Portfolio API",
)

app.include_router(router=router_v1, prefix="/api/v1")
