from app.domain.repositories.stock_repository import StockRepository


class StockService:
    def __init__(self, repo: StockRepository):
        self.repo = repo

    def get_stock(self, user_id: int):
        return self.repo.get_by_id(user_id)

    def get_all_stocks(self):
        return self.repo.list_stocks()
