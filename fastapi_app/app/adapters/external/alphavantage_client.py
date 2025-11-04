# app/adapters/external/alphavantage_client.py
import httpx


class AlphaVantageClient:
    BASE_URL = "https://www.alphavantage.co/query"
    API_KEY = "Y3E5063QA9MVU741"

    async def get_stock_overview(self, symbol: str):
        params = {
            "function": "OVERVIEW",
            "symbol": symbol,
            "apikey": self.API_KEY,
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()