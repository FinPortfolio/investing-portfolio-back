from abc import ABC, abstractmethod
from app.domain.entities.stock import StockEntity


class StockRepository(ABC):
    @abstractmethod
    def get_by_id(self, stock_id: int) -> StockEntity: ...

    @abstractmethod
    def list_stocks(self) -> list[StockEntity]: ...

