from sqlalchemy import Column, Integer, String
from app.adapters.db.session import Base


class StockModel(Base):
    __tablename__ = "stocks"

    stock_id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, index=True)
    name = Column(String)
