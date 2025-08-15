from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from fastapi_app.app.interfaces.api.v1 import router as router_v1
from fastapi_app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Investing Portfolio API",
)

app.include_router(
    router=router_v1,
    prefix=settings.api.prefix
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
