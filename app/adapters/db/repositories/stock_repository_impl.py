# adapters/db/stock_repository_impl.py
from app.adapters.db.models.stock_model import StockModel
from app.application.exceptions import EntityNotFoundError
from app.domain.entities.stock import StockEntity
from app.domain.repositories.stock_repository import StockRepository


class SQLAlchemyStockRepository(StockRepository):

    def __init__(self, session):
        self.session = session

    def list_stocks(self) -> list[StockEntity]:
        return [
            StockEntity(
                stock_id=stock.stock_id,
                symbol=stock.symbol,
                name=stock.name
            )
            for stock in self.session.query(StockModel).all()
        ]

    def create_stock(self, stock: StockEntity) -> StockEntity:
        stock_db = StockModel(
            symbol=stock.symbol,
            name=stock.name
        )
        self.session.add(stock_db)
        self.session.commit()
        self.session.refresh(stock_db)
        return StockEntity(
            stock_id=stock_db.stock_id,
            symbol=stock_db.symbol,
            name=stock_db.name
        )

    def get_by_id(self, stock_id: int) -> StockEntity:
        stock = self.session.get(StockModel, stock_id)
        if stock is None:
            raise EntityNotFoundError()
        return StockEntity(
            stock_id=stock.stock_id,
            symbol=stock.symbol,
            name=stock.name
        )
