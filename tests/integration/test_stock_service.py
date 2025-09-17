import pytest

from httpx import AsyncClient

@pytest.mark.asyncio
async def test_read_stocks(client: AsyncClient):
    stock_payloads = [
        {"name": "Apple Inc.", "symbol": "AAPL"},
        {"name": "Tesla Inc.", "symbol": "TSLA"},
    ]

    for payload in stock_payloads:
        response = await client.post("/api/v1/stocks/", json=payload)
        assert response.status_code == 201

    response = await client.get("/api/v1/stocks/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == len(stock_payloads)

    names = [item["name"] for item in data]
    symbols = [item["symbol"] for item in data]

    for payload in stock_payloads:
        assert payload["name"] in names
        assert payload["symbol"] in symbols


@pytest.mark.asyncio
async def test_read_stocks_2(client: AsyncClient):
    stock_payloads = [
        {"name": "Bitcoin", "symbol": "BTC"},
        {"name": "Etherium", "symbol": "ETH"},
    ]

    for payload in stock_payloads:
        response = await client.post("/api/v1/stocks/", json=payload)
        assert response.status_code == 201

    response = await client.get("/api/v1/stocks/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == len(stock_payloads)

    names = [item["name"] for item in data]
    symbols = [item["symbol"] for item in data]

    for payload in stock_payloads:
        assert payload["name"] in names
        assert payload["symbol"] in symbols


@pytest.mark.asyncio
async def test_create_stock(client: AsyncClient):
    payload = {
        "name": "Tesla Inc.",
        "symbol": "TSLA"
    }

    response = await client.post("/api/v1/stocks/", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["symbol"] == payload["symbol"]

    assert "stock_id" in data


@pytest.mark.asyncio
async def test_create_stock_2(client: AsyncClient):
    payload = {
        "name": "IBM Inc.",
        "symbol": "IBM"
    }

    response = await client.post("/api/v1/stocks/", json=payload)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["symbol"] == payload["symbol"]

    assert "stock_id" in data