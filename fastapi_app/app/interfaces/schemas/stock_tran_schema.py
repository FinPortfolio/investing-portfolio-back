# app.interfaces.schemas.stock_tran_schema.py
from __future__ import annotations

from datetime import date

from pydantic import BaseModel

from app.domain.entities import AssetType, StockTranEntity, TransactionCurrency, TransactionType


class StockTranBase(BaseModel):
    asset_type: AssetType
    asset_id: int
    provider: str
    initial_price: float
    transaction_commission: float
    transaction_currency: TransactionCurrency
    transaction_date: date
    transaction_quantity: float
    transaction_type: TransactionType
    notes: str


class StockTranPublic(StockTranBase):
    transaction_id: int

    @classmethod
    def from_entity(cls, entity: StockTranEntity) -> StockTranPublic:
        # import json
        # from enum import Enum
        # from datetime import date
        # def default_converter(o):
        #     if isinstance(o, date):
        #         return o.isoformat()  # date → 'YYYY-MM-DD'
        #     if isinstance(o, Enum):
        #         return o.value  # Enum → его значение
        #     return str(o)
        # data = entity.__dict__
        # print("DICT________________________:", json.dumps(data, indent=4, default=default_converter))
        return cls(
            transaction_id=entity.transaction_id,
            asset_type=entity.asset_type,
            asset_id=entity.asset_id,
            provider=entity.provider,
            initial_price=entity.initial_price,
            transaction_commission=entity.transaction_commission,
            transaction_currency=entity.transaction_currency,
            transaction_date=entity.transaction_date,
            transaction_quantity=entity.transaction_quantity,
            transaction_type=entity.transaction_type,
            notes=entity.notes,
        )
        # data = entity.__dict__
        # return cls(**data)


class StockTranCreate(StockTranBase):
    pass