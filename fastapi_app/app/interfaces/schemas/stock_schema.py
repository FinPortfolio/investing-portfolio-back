from __future__ import annotations

from pydantic import BaseModel

from app.domain.entities import StockEntity


class StockBase(BaseModel):
    symbol: str
    name: str


class Stock(StockBase):
    stock_id: int


class StockPublic(StockBase):
    stock_id: int

    @classmethod
    def from_entity(cls, entity: StockEntity) -> StockPublic:
        return cls(
            stock_id=entity.stock_id,
            symbol=entity.symbol,
            name=entity.name,
        )


class StockCreate(StockBase):
    pass

    # def to_entity(self) -> StockEntity:
    #     return StockEntity(
    #         symbol=self.symbol,
    #         name=self.name,
    #     )


class StockFullUpdate(StockCreate):
    pass


class StockPartialUpdate(StockBase):
    symbol: str | None = None
    name: str | None = None
