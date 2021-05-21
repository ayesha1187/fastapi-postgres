"""insert_queries

Revision ID: df6f2c7ed8e5
Revises: c56a5627c415
Create Date: 2021-05-13 22:18:06.073157

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime 

# revision identifiers, used by Alembic.
revision = 'df6f2c7ed8e5'
down_revision = 'c56a5627c415'
branch_labels = None
depends_on = None


def upgrade():
    
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Bond','counterparty01','TSLA01','ins01','T01','Trader01')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Bond','counterparty02','TSLA01','ins01','T02','Trader01')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Fix','counterparty03','TSLA02','ins02','T03','Trader02')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Equity','counterparty03','TSLA02','ins02','T04','Trader02')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Bond','counterparty03','TSLA01','ins01','T05','Trader03')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Equity','counterparty04','TSLA03','ins03','T06','Trader03')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Equity','counterparty05','TSLA04','ins04','T07','Trader04')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Fix','counterparty06','TSLA05','ins05','T08','Trader05')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Bond','counterparty07','TSLA06','ins06','T09','Trader06')")
    op.execute("INSERT INTO public.t_trade(asset_class,counterparty,instrument_id,instrument_name,trade_id,trader) VALUES ('Bond','counterparty07','TSLA07','ins07','T10','Trader07')")

    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T01','buy',10.5,5)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T02','buy',11.75,10)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T03','sell',15.80,20)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T04','sell',15.75,30)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T05','sell',18.20,50)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T06','buy',9.5,5)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T07','buy',10,40)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T08','buy',12,30)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T09','sell',20.25,40)")
    op.execute("INSERT INTO public.t_trade_details(trade_id ,buysellindicator,price ,quantity) VALUES ('T10','sell',25.75,50)")

def downgrade():
    pass
