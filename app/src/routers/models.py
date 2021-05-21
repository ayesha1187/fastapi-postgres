from typing import Optional,List
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class TradeDetails(BaseModel):
    buysellindicator: str = Field(alias="buysellindicator", description="A value of BUY for buys, SELL for sells")
    price: float = Field(alias="price", description="The price of the Trade")
    quantity: int = Field(alias="quantity", description="The amount of units traded")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass")
    counterparty: Optional[str] = ""
    instrument_id: str = Field(alias="instrumentId")
    instrument_name: str = Field(alias="instrumentName")
    trade_date_time: str = Field(alias="tradeDateTime")
    trade_id: str = Field(alias="tradeId")
    trader: str = Field(description="name of the trader")
    trade_details: TradeDetails = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class FilterCriteria(BaseModel):
    assetClass: Optional[str] = None
    end: Optional[str] = None
    maxPrice: Optional[str] = None
    minPrice: Optional[str] = None
    start: Optional[str] = None
    tradeType: Optional[str] = None
