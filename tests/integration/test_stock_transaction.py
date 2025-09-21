import pytest

from httpx import AsyncClient

from tests.constants import StockTranConst

@pytest.mark.asyncio
@pytest.mark.parametrize(
    "payload",
    StockTranConst.PAYLOAD_FOR_CREATE_STOCK_TRAN,
)
async def test_read_stock_transactions(
        client: AsyncClient,
        payload: dict,
):
    response = await client.post("/api/v1/stock_transactions/", json=payload)
    assert response.status_code == 201

    response = await client.get("/api/v1/stock_transactions/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)


    # names = [item["name"] for item in data]
    # symbols = [item["symbol"] for item in data]
    #
    # for payload in stock_transactions_payloads:
    #     assert payload["name"] in names
    #     assert payload["symbol"] in symbols