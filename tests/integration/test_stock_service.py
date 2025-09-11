import unittest
from fastapi_app.app.application.services.stock_service import StockService
from fastapi_app.app.application.exceptions import StockNotFoundError
from fastapi_app.app.adapters.db.repositories.stock_repository_impl import StockRepositoryImpl
from fastapi_app.app.adapters.db.pg_db_manager import PgDbManager
from fastapi_app.app.domain.entities.stock import StockEntity


class TestStockServiceIntegration(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        # создаём тестовое подключение к БД
        self.session_maker = await PgDbManager.create_test_session()
        self.repo = StockRepositoryImpl(self.session_maker)
        self.service = StockService(self.repo)

        # очищаем таблицу перед каждым тестом
        async with self.session_maker() as session:
            await session.execute("TRUNCATE TABLE stocks RESTART IDENTITY CASCADE;")
            await session.commit()

    async def test_add_and_get_stock(self):
        stock_data = {"ticker": "AAPL", "price": 150.0}
        created = await self.service.add_stock(stock_data)

        self.assertIsInstance(created, StockEntity)
        self.assertEqual(created.ticker, "AAPL")
        self.assertEqual(created.price, 150.0)

        fetched = await self.service.get_stock(created.id)
        self.assertEqual(fetched.id, created.id)
        self.assertEqual(fetched.ticker, "AAPL")

    async def test_get_all_stocks(self):
        await self.service.add_stock({"ticker": "AAPL", "price": 150.0})
        await self.service.add_stock({"ticker": "MSFT", "price": 250.0})

        stocks = await self.service.get_all_stocks()
        tickers = [s.ticker for s in stocks]

        self.assertIn("AAPL", tickers)
        self.assertIn("MSFT", tickers)