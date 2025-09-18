from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.adapters.db.models import Base
from app.domain.entities import StockTranEntity


class StockTranModel(Base):
    __tablename__ = "stock_trans"

    stock_tran_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    asset_type: Mapped[str] = mapped_column(String(10), nullable=False)
    initial_price: Mapped[float] = mapped_column(nullable=False)
    transaction_commission: Mapped[float] = mapped_column(nullable=False)
    transaction_currency: Mapped[str] = mapped_column(String(10), nullable=False)
    transaction_date: Mapped[str] = mapped_column(Date, nullable=False)
    transaction_quantity: Mapped[float] = mapped_column(nullable=False)
    transaction_type: Mapped[str] = mapped_column(String(10), nullable=False)
    notes: Mapped[str | None] = mapped_column(String(255), nullable=True)

    def to_entity(self) -> StockTranEntity:
        return StockTranEntity(
            stock_tran_id=self.stock_tran_id,
            asset_type=self.asset_type,
            initial_price=self.initial_price,
            transaction_commission=self.transaction_commission,
            transaction_currency=self.transaction_currency,
            transaction_date=self.transaction_date,
            transaction_quantity=self.transaction_quantity,
            transaction_type=self.transaction_type,
            notes=self.notes,
        )
