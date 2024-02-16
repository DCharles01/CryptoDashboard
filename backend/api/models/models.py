from sqlalchemy import  create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class CryptoPrices(Base):
    __tablename__ = 'crypto_prices'

    id = Column(Integer, primary_key=True)
    symbol = Column(String, nullable=False)
    price_usd = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Cryptocurrency(Base):
    __tablename__ = 'cryptocurrencies'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    symbol = Column(String,)


