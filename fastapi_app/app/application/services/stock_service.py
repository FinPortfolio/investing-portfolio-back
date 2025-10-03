# app/application/services/stock_service.py
from app.domain.entities import StockEntity
from app.domain.repositories import StockRepository


class StockService:
    def __init__(self, repo: StockRepository):
        self.repo = repo

    async def get_all_stocks(self) -> list[StockEntity]:
        list_of_stocks = await self.repo.get_list_of_stocks()
        return list_of_stocks

    # async def add_stock(self, stock: StockEntity):
    async def add_stock(self, stock: dict) -> StockEntity:
        db_stock_entity = await self.repo.create_stock(stock)
        return db_stock_entity

    async def get_stock(self, stock_id: int) -> StockEntity:
        db_stock_entity = await self.repo.get_stock_by_id(stock_id)
        return db_stock_entity

    async def update_stock(self, stock_id: int, stock: dict) -> StockEntity:
        db_stock_entity = await self.repo.update_stock(stock_id, stock)
        return db_stock_entity

    async def delete_stock(self, stock_id: int) -> None:
        await self.repo.delete_stock(stock_id)
