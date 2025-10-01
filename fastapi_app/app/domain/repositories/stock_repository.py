# app/domain/repositories/stock_repository.py
from abc import ABC, abstractmethod

from app.domain.entities import StockEntity


class StockRepository(ABC):

    @abstractmethod
    async def get_list_of_stocks(self) -> list[StockEntity]: ...

    @abstractmethod
    # async def create_stock(self, stock: StockEntity) -> StockEntity: ...
    async def create_stock(self, stock: dict) -> StockEntity: ...

    @abstractmethod
    async def get_stock_by_id(self, stock_id: int) -> StockEntity: ...

    @abstractmethod
    async def get_stock_by_ticker_or_404(self, ticker: str) -> StockEntity: ...

    @abstractmethod
    async def update_stock(self, stock_id: int, stock: dict) -> StockEntity: ...

    @abstractmethod
    async def delete_stock(self, stock_id: int) -> None: ...
