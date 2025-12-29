from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.interfaces.api.v1 import router_v1
from core.config import settings
from app.adapters.db import pg_db_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await pg_db_manager.dispose()


main_app = FastAPI(
    lifespan=lifespan,
    title="Investing Portfolio API",
)

ORIGINS = [
    "http://investing-portfolio.pl",
    "https://investing-portfolio.pl",
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
]

main_app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main_app.include_router(
    router=router_v1,
    prefix=settings.api.prefix
)


@main_app.get("/")
async def read_stocks():
    return {"message": "Everything is OK!!!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
