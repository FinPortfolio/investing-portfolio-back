class StockTranEntity:

    def __init__(
            self,
            asset_type = str,
            # symbol_id = str,  # Foreign Key for table "Stocks"
            initial_price = float,
            # provider = dict,  # Nested object or not?
            transaction_commission = float,
            transaction_currency = str,
            transaction_date = str,
            transaction_quantity = float,
            transaction_type = str,
            notes = str,
            stock_tran_id: int | None = None,
    ):
        self.stock_tran_id = stock_tran_id
        self.asset_type = asset_type
        self.initial_price = initial_price
        self.transaction_commission = transaction_commission
        self.transaction_currency = transaction_currency
        self.transaction_date = transaction_date
        self.transaction_quantity = transaction_quantity
        self.transaction_type = transaction_type
        self.notes = notes
