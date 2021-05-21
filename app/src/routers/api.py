from fastapi import APIRouter, Request, Depends
import logging
from typing import List, Optional
from datetime import datetime

from fastapi.param_functions import Body
from src.routers.models import Trade,FilterCriteria
from src.helpers import api_helper

logger = logging.getLogger()
logger.setLevel(logging.INFO)

api_router = APIRouter()

# @api_router.get("/getalltrades/" , response_model = List[Trade])
@api_router.get("/getalltrades/", response_model=List[Trade])
def get_all_trades():
    return api_helper.get_all_trades()

@api_router.get("/gettradedetails/{trade_id}", response_model=List[Trade])
def get_all_trades(trade_id: str):
    return api_helper.get_details_by_trade_id(trade_id)

@api_router.get("/searchtrade/",response_model=List[Trade])
def search_by_criteria(request: Request):
    result = []
    params = dict((k, v) for k, v in request.query_params.items())
    for value in params.values():
        result = api_helper.search_by_criteria(value)
    return result

@api_router.get("/filtercriteria/")
def search_by_advance_criteria(filtercriteria: dict = Depends(FilterCriteria)):
    result = api_helper.search_by_advance_criteria(filtercriteria)
    return result