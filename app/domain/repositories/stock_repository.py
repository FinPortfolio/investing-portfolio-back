from abc import ABC, abstractmethod
from app.domain.entities.stock import StockEntity


class StockRepository(ABC):

    @abstractmethod
    def list_stocks(self) -> list[StockEntity]: ...

    @abstractmethod
    def create_stock(self, stock: StockEntity) -> StockEntity: ...

    @abstractmethod
    def get_by_id(self, stock_id: int) -> StockEntity: ...