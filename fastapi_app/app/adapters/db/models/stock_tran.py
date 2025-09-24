# app/adapters/db/models/stock_tran.py
from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.adapters.db.models import Base
from app.domain.entities import AssetType, StockTranEntity, TransactionCurrency, TransactionType

if TYPE_CHECKING:
    from app.adapters.db.models import StockModel


class StockTranModel(Base):
    __tablename__ = "stock_trans"

    stock_tran_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    asset_type: Mapped[AssetType] = mapped_column(
        Enum(
            AssetType,
            name="asset_type_enum",
            values_callable=lambda enum: [e.value for e in enum]
        ),
        nullable=False
    )
    symbol_id: Mapped[str] = mapped_column(ForeignKey("stocks.symbol"))
    symbol: Mapped["StockModel"] = relationship(back_populates="stock_transactions")
    initial_price: Mapped[float] = mapped_column(nullable=False)
    transaction_commission: Mapped[float] = mapped_column(nullable=False)
    transaction_currency: Mapped[TransactionCurrency] = mapped_column(
        Enum(
            TransactionCurrency,
            name="transaction_currency_enum",
            values_callable=lambda enum: [e.value for e in enum]
        ),
        nullable=False
    )
    transaction_date: Mapped[date] = mapped_column(Date, nullable=False)
    transaction_quantity: Mapped[float] = mapped_column(nullable=False)
    transaction_type: Mapped[TransactionType] = mapped_column(
        Enum(
            TransactionType,
            name="transaction_type_enum",
            values_callable=lambda enum: [e.value for e in enum]
        ),
        nullable=False
    )
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
