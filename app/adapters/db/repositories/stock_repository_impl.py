# adapters/db/stock_repository_impl.py
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.models import StockModel
from app.application.exceptions import EntityNotFoundError
from app.domain.entities import StockEntity
from app.domain.repositories import StockRepository


class SQLAlchemyStockRepository(StockRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_db_stock_or_404(self, stock_id: int) -> StockModel:
        db_stock: StockModel | None = await self.session.get(StockModel, stock_id)
        if db_stock is None:
            raise EntityNotFoundError()
        return db_stock

    async def get_list_of_stocks(self) -> list[StockEntity]:
        statement = select(StockModel).order_by(StockModel.stock_id)
        result: Result = await self.session.execute(statement)
        db_stocks = result.scalars().all()
        return [db_stock.to_entity() for db_stock in db_stocks]

    async def create_stock(self, stock: dict) -> StockEntity:
        db_stock = StockModel(**stock)
        self.session.add(db_stock)
        await self.session.commit()
        return db_stock.to_entity()

    async def get_stock_by_id(self, stock_id: int) -> StockEntity:
        db_stock = await self._get_db_stock_or_404(stock_id)
        return db_stock.to_entity()

    async def update_stock(self, stock_id: int, stock: dict) -> StockEntity:
        db_stock = await self._get_db_stock_or_404(stock_id)
        for field, value in stock.items():
            setattr(db_stock, field, value)
        await self.session.commit()
        return db_stock.to_entity()

    async def delete_stock(self, stock_id: int) -> None:
        db_stock = await self._get_db_stock_or_404(stock_id)
        await self.session.delete(db_stock)
        await self.session.commit()
