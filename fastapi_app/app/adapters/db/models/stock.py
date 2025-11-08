# app/adapters/db/models/stock.py
from typing import TYPE_CHECKING

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.db.models import Base
from app.domain.entities import StockEntity


if TYPE_CHECKING:
    from app.adapters.db.models import StockTranModel


class StockModel(Base):
    __tablename__ = "stocks"

    stock_id: Mapped[int] = mapped_column(primary_key=True)
    symbol: Mapped[str] = mapped_column(String(20), unique=True)
    provider: Mapped[str] = mapped_column(String(50))
    name: Mapped[str] = mapped_column(String(200), nullable=True)
    transactions: Mapped[list["StockTranModel"]] = relationship(
        back_populates="asset",
        uselist=True,
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        UniqueConstraint(
            "symbol", "provider", name="uq_symbol_provider"
        ),
    )

    def to_entity(self) -> StockEntity:
        return StockEntity(
            stock_id=self.stock_id,
            symbol=self.symbol,
            provider=self.provider,
            name=self.name,
        )
