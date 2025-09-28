from datetime import date
from enum import StrEnum


class AssetType(StrEnum):
    STOCK = "stock"
    ETF = "etf"
    BOND = "bond"
    CRYPTO = "crypto"


class TransactionCurrency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"


class TransactionType(StrEnum):
    BUY = "buy"
    SELL = "sell"


class StockTranEntity:

    def __init__(
            self,
            asset_type: AssetType,
            symbol_id: str,  # Foreign Key for table "Stocks"
            initial_price: float,
            # provider: dict,  # Nested object or not?
            transaction_commission: float,
            transaction_currency: TransactionCurrency,
            transaction_date: date,
            transaction_quantity: float,
            transaction_type: TransactionType,
            notes: str,
            transaction_id: int | None = None,
    ):
        self.transaction_id = transaction_id
        self.asset_type = asset_type
        self.symbol_id = symbol_id
        self.initial_price = initial_price
        self.transaction_commission = transaction_commission
        self.transaction_currency = transaction_currency
        self.transaction_date = transaction_date
        self.transaction_quantity = transaction_quantity
        self.transaction_type = transaction_type
        self.notes = notes
