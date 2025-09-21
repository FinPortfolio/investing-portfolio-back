# app/application/services/stock_tran_service.py
from app.application.exceptions import (
    EntityNotFoundError,
    StockNotFoundError,
    StockTranNotFoundError,
)
from app.domain.entities import StockTranEntity
from app.domain.repositories import StockTranRepository


class StockTranService:
    def __init__(self, repo: StockTranRepository):
        self.repo = repo

    async def get_all_stock_transactions(self) -> list[StockTranEntity]:
        list_of_stocks = await self.repo.get_list_of_stock_transactions()
        return list_of_stocks

    async def add_stock_tran(self, stock_tran: dict) -> StockTranEntity:
        db_stock_tran_entity = await self.repo.create_stock_transaction(stock_tran)
        return db_stock_tran_entity

    async def get_stock(self, stock_tran_id: int) -> StockTranEntity:
        try:
            db_stock_tran_entity = await self.repo.get_stock_tran_by_id(stock_tran_id)
        except EntityNotFoundError:
            raise StockTranNotFoundError()
        return db_stock_tran_entity
    #
    # async def update_stock(self, stock_id: int, stock: dict) -> StockEntity:
    #     try:
    #         db_stock_entity = await self.repo.update_stock(stock_id, stock)
    #     except EntityNotFoundError:
    #         raise StockNotFoundError()
    #     return db_stock_entity
    #
    # async def delete_stock(self, stock_id: int) -> None:
    #     try:
    #         await self.repo.delete_stock(stock_id)
    #     except EntityNotFoundError:
    #         raise StockNotFoundError()
