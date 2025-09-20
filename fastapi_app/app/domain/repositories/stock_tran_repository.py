# app/domain/repositories/stock_tran_repository.py
from abc import ABC, abstractmethod

from app.domain.entities import StockTranEntity


class StockTranRepository(ABC):

    @abstractmethod
    async def get_list_of_stock_transactions(self) -> list[StockTranEntity]: ...

    @abstractmethod
    async def create_stock_transaction(self, stock_tran: dict) -> StockTranEntity: ...

    @abstractmethod
    async def get_stock_tran_by_id(self, stock_tran_id: int) -> StockTranEntity: ...
