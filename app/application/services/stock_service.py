# app/application/services/stock_service.py
from app.application.exceptions import EntityNotFoundError, StockNotFoundError
from app.domain.entities.stock import StockEntity
from app.domain.repositories.stock_repository import StockRepository


class StockService:
    def __init__(self, repo: StockRepository):
        self.repo = repo

    def get_all_stocks(self):
        return self.repo.list_stocks()

    def add_stock(self, stock: StockEntity):
        return self.repo.create_stock(stock)

    def get_stock(self, stock_id: int):
        try:
            stock = self.repo.get_by_id(stock_id)
        except EntityNotFoundError:
            # обработка ошибки, например:
            raise StockNotFoundError()
        return stock
