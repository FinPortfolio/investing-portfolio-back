from app.domain.entities.stock import StockEntity
from app.domain.repositories.stock_repository import StockRepository
from app.adapters.db.models.user_model import StockModel


class SQLAlchemyStockRepository(StockRepository):
    def __init__(self, session):
        self.session = session

    def get_by_id(self, stock_id: int) -> StockEntity:
        obj = self.session.query(StockModel).get(stock_id)
        return StockEntity(
            stock_id=obj.stock_id,
            symbol=obj.symbol,
            name=obj.name
        )

    def list_users(self) -> list[StockEntity]:
        return [
            StockEntity(
                stock_id=obj.stock_id,
                symbol=obj.symbol,
                name=obj.name
            )
            for obj in self.session.query(StockModel).all()
        ]
