# app/application/services/stock_tran_service.py
from app.domain.entities import StockTranEntity
from app.domain.repositories import StockRepository, StockTranRepository


class StockTranService:
    def __init__(self, tran_repo: StockTranRepository, stock_repo: StockRepository):
        self.tran_repo = tran_repo
        self.stock_repo = stock_repo

    async def get_all_stock_transactions(self) -> list[StockTranEntity]:
        list_of_stocks = await self.tran_repo.get_list_of_stock_transactions()
        return list_of_stocks

    async def add_stock_tran(self, stock_tran_data: dict) -> StockTranEntity:
        ticker = stock_tran_data.pop("asset_ticker")
        db_stock_entity = await self.stock_repo.get_stock_by_ticker_or_500(ticker)
        stock_tran_data["asset_id"] = db_stock_entity.stock_id
        return await self.tran_repo.create_stock_transaction(stock_tran_data)

    async def get_stock_tran(self, transaction_id: int) -> StockTranEntity:
        db_stock_tran_entity = await self.tran_repo.get_stock_tran_by_id(transaction_id)
        return db_stock_tran_entity

    async def delete_stock_tran(self, transaction_id: int) -> None:
        await self.tran_repo.delete_stock_tran(transaction_id)
