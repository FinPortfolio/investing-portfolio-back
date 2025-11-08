# app.interfaces.schemas.stock_schema.py
from __future__ import annotations

from pydantic import BaseModel

from app.domain.entities import StockEntity


class StockBase(BaseModel):
    symbol: str
    provider: str
    name: str


class Stock(StockBase):
    stock_id: int


class StockPublic(StockBase):
    stock_id: int
    name: str | None

    @classmethod
    def from_entity(cls, entity: StockEntity) -> StockPublic:
        return cls(
            stock_id=entity.stock_id,
            symbol=entity.symbol,
            provider=entity.provider,
            name=entity.name,
        )


class StockCreate(StockBase):
    pass


class StockFullUpdate(StockCreate):
    pass


class StockPartialUpdate(StockBase):
    symbol: str | None = None
    provider: str | None = None
    name: str | None = None
