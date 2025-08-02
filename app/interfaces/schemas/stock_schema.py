from pydantic import BaseModel


class StockBase(BaseModel):
    symbol: str
    name: str

class Stock(StockBase):
    stock_id: int

class StockPublic(StockBase):
    stock_id: int

class StockCreate(StockBase):
    pass

class StockUpdate(StockBase):
    symbol: str | None = None
    name: str | None = None