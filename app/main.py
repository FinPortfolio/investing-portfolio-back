from fastapi import FastAPI

from app.adapters.db.session import engine, Base
from app.interfaces.api.v1 import stock_routes

app = FastAPI(title="Investing Portfolio API")

Base.metadata.create_all(bind=engine)

app.include_router(stock_routes.router, prefix="/api/v1", tags=["stocks"])

@app.get("/")
def root():
    return {"message": "Welcome to Investing Portfolio API"}
