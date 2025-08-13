from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from fastapi_app.app.adapters.db.models import Base
from fastapi_app.app.domain.entities import StockEntity


class StockModel(Base):
    __tablename__ = "stocks"

    stock_id: Mapped[int] = mapped_column(primary_key=True)
    symbol: Mapped[str] = mapped_column(String(5))
    name: Mapped[str] = mapped_column(String(50))

    def to_entity(self) -> StockEntity:
        return StockEntity(
            stock_id=self.stock_id,
            symbol=self.symbol,
            name=self.name
        )
