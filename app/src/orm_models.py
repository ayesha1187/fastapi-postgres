from sqlalchemy import Column,DateTime,ForeignKey,Integer,Numeric,Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

    
class TTrade(Base):
    __tablename__ = 't_trade'

    asset_class = Column(Text)
    counterparty = Column(Text)
    instrument_id = Column(Text)
    instrument_name = Column(Text)
    trade_date_time = Column(DateTime(True))
    trade_id = Column(Text, primary_key=True)
    trader = Column(Text)

class TTradeDetails(Base):
    __tablename__ = 't_trade_details'

    trade_details_id = Column(Integer, primary_key=True, autoincrement=True)
    trade_id = Column(ForeignKey('t_trade.trade_id'), nullable=False)
    buysellindicator = Column(Text)
    price = Column(Numeric)
    quantity = Column(Integer)
    
    trade = relationship('TTrade')

