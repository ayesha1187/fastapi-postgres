import logging
from src.helpers import db_helper

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_all_trades():
    return db_helper.get_all_trades()

def get_details_by_trade_id(trade_id):
    return db_helper.get_details_by_trade_id(trade_id)

def search_by_criteria(value):
    return db_helper.search_by_criteria(value)

def search_by_advance_criteria(filtercriteria):
    return db_helper.search_by_advance_criteria(filtercriteria)