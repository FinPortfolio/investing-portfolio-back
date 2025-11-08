# app/adapters/db/stock_repository_impl.py
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.db.models import StockModel
from app.adapters.exceptions import StockAlreadyExistsError, StockNotFoundError
from app.domain.entities import StockEntity
from app.domain.repositories import StockRepository


class SQLAStockRepository(StockRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def _get_db_stock_or_500(self, stock_id: int) -> StockModel:
        db_stock: StockModel | None = await self.session.get(StockModel, stock_id)
        if db_stock is None:
            raise StockNotFoundError()
        return db_stock

    async def get_stock_by_ticker_or_500(self, ticker: str) -> StockEntity:
        stmt = select(StockModel).where(StockModel.symbol == ticker)
        result = await self.session.execute(stmt)
        stock = result.scalar_one_or_none()
        if stock is None:
            raise StockNotFoundError(f"Stock with ticker '{ticker}' not found")
        return stock.to_entity()

    async def get_or_create_stock(self, symbol: str, provider: str) -> StockEntity:
    # async def get_or_create_stock(self, ticker: str) -> StockEntity:
        async def _get_stock():
            stmt = select(StockModel).where(
                StockModel.symbol == symbol,
                StockModel.provider == provider,
            )
            result = await self.session.execute(stmt)
            return result.scalar_one_or_none()

        stock = await _get_stock()
        if stock:
            return stock.to_entity()

        new_stock = StockModel(symbol=symbol, provider=provider)
        # new_stock = StockModel(symbol=symbol)
        self.session.add(new_stock)

        try:
            await self.session.commit()
        except IntegrityError:
            # if someone added the same one at the same time
            await self.session.rollback()
            stock = await _get_stock()
            if not stock:
                raise StockAlreadyExistsError
            return stock.to_entity()

        await self.session.refresh(new_stock)
        return new_stock.to_entity()

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
        db_stock = await self._get_db_stock_or_500(stock_id)
        return db_stock.to_entity()

    async def update_stock(self, stock_id: int, stock: dict) -> StockEntity:
        db_stock = await self._get_db_stock_or_500(stock_id)
        for field, value in stock.items():
            setattr(db_stock, field, value)
        await self.session.commit()
        return db_stock.to_entity()

    async def delete_stock(self, stock_id: int) -> None:
        db_stock = await self._get_db_stock_or_500(stock_id)
        await self.session.delete(db_stock)
        await self.session.commit()
