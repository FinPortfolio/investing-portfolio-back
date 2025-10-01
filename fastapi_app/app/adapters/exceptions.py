# app/adapters/exceptions.py


class RepoError(Exception):

    default_message = "An unexpected exception occurred"

    def __init__(self, message=None):
        if message is None:
            self.message = self.default_message
        super().__init__(self.message)


class StockNotFoundError(RepoError):

    default_message = "Stock not found"


class StockTranNotFoundError(RepoError):

    default_message = "Stock Transaction not found"
