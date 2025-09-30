# app/adapters/db/stock_tran_repository_impl.py
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.models import StockTranModel
from app.application.exceptions import EntityNotFoundError
from app.domain.entities import StockTranEntity
from app.domain.repositories import StockTranRepository


class SQLAStockTranRepository(StockTranRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_db_stock_tran_or_404(self, transaction_id: int) -> StockTranModel:
        db_stock_tran: StockTranModel | None = await self.session.get(StockTranModel, transaction_id)
        if db_stock_tran is None:
            raise EntityNotFoundError()
        return db_stock_tran

    async def get_list_of_stock_transactions(self) -> list[StockTranEntity]:
        statement = select(StockTranModel).order_by(StockTranModel.transaction_id)
        result: Result = await self.session.execute(statement)
        db_stock_trans = result.scalars().all()
        return [db_stock_tran.to_entity() for db_stock_tran in db_stock_trans]

    async def create_stock_transaction(self, stock_tran: dict) -> StockTranEntity:
        db_stock_tran = StockTranModel(**stock_tran)
        self.session.add(db_stock_tran)
        await self.session.commit()
        return db_stock_tran.to_entity()

    async def get_stock_tran_by_id(self, transaction_id: int) -> StockTranEntity:
        db_stock_tran = await self._get_db_stock_tran_or_404(transaction_id)
        return db_stock_tran.to_entity()

    async def delete_stock_tran(self, transaction_id: int) -> None:
        db_stock_tran = await self._get_db_stock_tran_or_404(transaction_id)
        await self.session.delete(db_stock_tran)
        await self.session.commit()