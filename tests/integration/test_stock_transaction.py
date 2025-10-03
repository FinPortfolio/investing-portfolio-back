import pytest

from httpx import AsyncClient

from fastapi import status
from tests.constants import (
    StockTranResponseConst,
    StockTranConst,
    UrlConstants
)


@pytest.mark.asyncio
async def test_get_stock_transactions(client: AsyncClient):
    response = await client.get(UrlConstants.STOCK_TRANS_ENDPOINT)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "payload",
    StockTranConst.PAYLOAD_FOR_CREATE_STOCK_TRAN,
)
async def test_create_stock_transaction(client: AsyncClient, payload: dict):
    response = await client.post(UrlConstants.STOCK_TRANS_ENDPOINT, json=payload)
    assert response.status_code == status.HTTP_201_CREATED, (
        f"Expected status 201 Created {response.status_code}, "
        f" received: {response.text}"
    )

    data = response.json()
    assert set(data.keys()) == StockTranResponseConst.EXPECTED_STOCK_TRAN_KEYS, (
        f"Expected response keys {StockTranResponseConst.EXPECTED_STOCK_TRAN_KEYS}, "
        f"received response keys {set(data.keys())}"
    )

    for field, expected_value in payload.items():
        assert data[field] == expected_value, (
            f"Expected response field value '{field}': '{expected_value}', "
            f"received response field value: '{data[field]}'"
        )
