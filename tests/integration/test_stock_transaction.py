import pytest

from httpx import AsyncClient

@pytest.mark.asyncio
async def test_read_stock_transactions(client: AsyncClient):
    stock_transactions_payloads = [
        {
            "asset_type": "stock",
            "symbol_id": "TSLA",
            "initial_price": 250.5,
            "provider": {
                "alphavantage": "https://www.alphavantage.co/query?symbol=TSLA"
            },
            "transaction_commision": 15.25,
            "transaction_currency": "USD",
            "transaction_date": "2025-09-15",
            "transaction_quantity": 165.4,
            "transaction_type": "sell",
            "notes": "Продажа после достижения целевой цены"
        },
        {
            "asset_type": "stock",
            "symbol_id": "IBM",
            "initial_price": 145.3,
            "provider": {
                "alphavantage": "https://www.alphavantage.co/query?symbol=IBM"
            },
            "transaction_commision": 7.5,
            "transaction_currency": "USD",
            "transaction_date": "2025-09-12",
            "transaction_quantity": 80,
            "transaction_type": "buy",
            "notes": "Покупка для дивидендного портфеля"
        }
    ]

    for payload in stock_transactions_payloads:
        response = await client.post("/api/v1/stock-transactions/", json=payload)
        assert response.status_code == 201

    response = await client.get("/api/v1/stock-transactions/")
    assert response.status_code == 200

    data = response.json()
    print("data: ", data)
    assert isinstance(data, list)
    assert len(data) == len(stock_transactions_payloads)

    # names = [item["name"] for item in data]
    # symbols = [item["symbol"] for item in data]
    #
    # for payload in stock_transactions_payloads:
    #     assert payload["name"] in names
    #     assert payload["symbol"] in symbols