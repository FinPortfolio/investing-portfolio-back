# app/adapters/db/stock_tran_repository_impl.py
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.models import StockTranModel
from app.application.exceptions import EntityNotFoundError
from app.domain.entities import StockTranEntity
from app.domain.repositories import StockTranRepository

class SQLAStockTranRepository(StockTranRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_db_stock_tran_or_404(self, stock_id: int) -> StockTranModel:
        db_stock_tran: StockTranModel | None = await self.session.get(StockTranModel, stock_id)
        if db_stock_tran is None:
            raise EntityNotFoundError()
        return db_stock_tran

    # async def create_stock(self, stock_tran: dict) -> StockTranEntity: ...

    async def get_stock_tran_by_id(self, stock_tran_id: int) -> StockTranEntity:
        db_stock_tran = await self._get_db_stock_tran_or_404(stock_tran_id)
        return db_stock_tran.to_entity()

    # async def delete_stock_tran(self, stock_tran_id: int) -> None: ...