from dataclasses import dataclass


@dataclass(frozen=True)
class UrlConstants:

    STOCK_TRANS_ENDPOINT: str = "/api/v1/stock_transactions/"


@dataclass(frozen=True)
class StockTranConst:

    PAYLOAD_FOR_CREATE_STOCK_TRAN: tuple[dict] = (
        {
            "asset_type": "stock",
            # "symbol_id": "TSLA",
            "initial_price": 250.5,
            # "provider": {
            #     "alphavantage": "https://www.alphavantage.co/query?symbol=TSLA"
            # },
            "transaction_commission": 15.25,
            "transaction_currency": "USD",
            "transaction_date": "2025-09-15",
            "transaction_quantity": 165.4,
            "transaction_type": "sell",
            "notes": "Продажа после достижения целевой цены"
        },
        {
            "asset_type": "stock",
            # "symbol_id": "IBM",
            "initial_price": 145.3,
            # "provider": {
            #     "alphavantage": "https://www.alphavantage.co/query?symbol=IBM"
            # },
            "transaction_commission": 7.5,
            "transaction_currency": "USD",
            "transaction_date": "2025-09-12",
            "transaction_quantity": 80,
            "transaction_type": "buy",
            "notes": "Покупка для дивидендного портфеля"
        },
    )


class StockTranResponseConst:

    SERVER_KEYS: set[str] = {"stock_tran_id"}
    PAYLOAD_KEYS: set[str] = set(StockTranConst.PAYLOAD_FOR_CREATE_STOCK_TRAN[0].keys())

    EXPECTED_STOCK_TRAN_KEYS = set(SERVER_KEYS | PAYLOAD_KEYS)
