# app.interfaces.schemas.stock_tran_schema.py
from __future__ import annotations

from datetime import date

from pydantic import BaseModel

from app.domain.entities import AssetType, StockTranEntity, TransactionCurrency, TransactionType


class StockTranBase(BaseModel):
    asset_type: AssetType
    initial_price: float
    transaction_commission: float
    transaction_currency: TransactionCurrency
    transaction_date: date
    transaction_quantity: float
    transaction_type: TransactionType
    notes: str


class StockTranPublic(StockTranBase):
    stock_tran_id: int

    @classmethod
    def from_entity(cls, entity: StockTranEntity) -> StockTranPublic:
        return cls(
            stock_tran_id=entity.stock_tran_id,
            asset_type=entity.asset_type,
            initial_price=entity.initial_price,
            transaction_commission=entity.transaction_commission,
            transaction_currency=entity.transaction_currency,
            transaction_date=entity.transaction_date,
            transaction_quantity=entity.transaction_quantity,
            transaction_type=entity.transaction_type,
            notes=entity.notes,
        )


class StockTranCreate(StockTranBase):
    pass