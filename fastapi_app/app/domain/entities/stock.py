class StockEntity:

    def __init__(
            self,
            symbol: str,
            name: str,
            stock_id: int | None = None,
    ):
        self.stock_id = stock_id
        self.symbol = symbol
        self.name = name
