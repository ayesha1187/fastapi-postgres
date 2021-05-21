from src.routers.models import FilterCriteria
from sqlalchemy.sql.schema import Column
from datetime import datetime, timedelta

from sqlalchemy import create_engine , or_ , and_
from sqlalchemy.orm import session, sessionmaker
from src.orm_models import TTrade, TTradeDetails
from os import environ as env
import base64


db_pass = base64.b64decode(env['DbPassword'].encode('ascii')).decode('ascii')

db_engine = create_engine(f"postgresql://{env['DbUser']}:{db_pass}@{env['DbUrl']}/{env['DbName']}")
Session = sessionmaker(bind=db_engine)

def get_all_trades():
    session = Session()
    data_list = []
    result =  [r for r in session.query(TTrade.asset_class,TTrade.counterparty,TTrade.instrument_id,TTrade.instrument_name,TTrade.trade_date_time,TTrade.trade_id,TTrade.trader,TTradeDetails.price,TTradeDetails.quantity,TTradeDetails.buysellindicator).filter(TTrade.trade_id == TTradeDetails.trade_id).order_by(TTrade.trader.asc()).limit(10).all()]
    for i in range(len(result)):
        data_list.append({"assetClass": result[i].asset_class,"counterparty":result[i].counterparty,"instrumentId":result[i].instrument_id,"instrumentName":result[i].instrument_name,"tradeDateTime":result[i].trade_date_time.strftime('%Y-%m-%d'),"tradeId":result[i].trade_id,"trader":result[i].trader,"trade_details":{"buysellindicator":result[i].buysellindicator,"price":result[i].price,"quantity":result[i].quantity}})
    return data_list

def get_details_by_trade_id(trade_id):
    session = Session()
    data_list = []
    result =  [r for r in session.query(TTrade.asset_class,TTrade.counterparty,TTrade.instrument_id,TTrade.instrument_name,TTrade.trade_date_time,TTrade.trade_id,TTrade.trader,TTradeDetails.price,TTradeDetails.quantity,TTradeDetails.buysellindicator).filter(TTrade.trade_id == TTradeDetails.trade_id).filter(TTrade.trade_id == trade_id).all()]
    for i in range(len(result)):
        data_list.append({"assetClass": result[i].asset_class,"counterparty":result[i].counterparty,"instrumentId":result[i].instrument_id,"instrumentName":result[i].instrument_name,"tradeDateTime":result[i].trade_date_time,"tradeId":result[i].trade_id,"trader":result[i].trader,"trade_details":{"buysellindicator":result[i].buysellindicator,"price":result[i].price,"quantity":result[i].quantity}})
    return data_list

def search_by_criteria(value):
    session = Session()
    data_list = []
    result = [r for r in session.query(TTrade.asset_class,TTrade.counterparty,TTrade.instrument_id,TTrade.instrument_name,TTrade.trade_date_time,TTrade.trade_id,TTrade.trader,TTradeDetails.price,TTradeDetails.quantity,TTradeDetails.buysellindicator).filter(TTrade.trade_id == TTradeDetails.trade_id).filter(or_(TTrade.counterparty == value, TTrade.instrument_id == value, TTrade.instrument_name == value,TTrade.trader == value)).all()]
    for i in range(len(result)):
        data_list.append({"assetClass": result[i].asset_class,"counterparty":result[i].counterparty,"instrumentId":result[i].instrument_id,"instrumentName":result[i].instrument_name,"tradeDateTime":result[i].trade_date_time,"tradeId":result[i].trade_id,"trader":result[i].trader,"trade_details":{"buysellindicator":result[i].buysellindicator,"price":result[i].price,"quantity":result[i].quantity}})
    return data_list

def search_by_advance_criteria(filtercriteria):
    session = Session()
    start = datetime.strptime(filtercriteria.start, '%Y-%m-%d')
    end = datetime.strptime(filtercriteria.end,'%Y-%m-%d') + timedelta(days=1)
    result = session.query(TTrade,TTradeDetails).filter(and_(TTrade.asset_class == filtercriteria.assetClass, TTradeDetails.buysellindicator == filtercriteria.tradeType, TTradeDetails.price >= filtercriteria.minPrice, TTradeDetails.price <= filtercriteria.maxPrice, TTradeDetails.trade_id == TTrade.trade_id, TTrade.trade_date_time >= start, TTrade.trade_date_time <= end)).order_by(TTrade.trader.asc()).limit(10).all()
    return result
