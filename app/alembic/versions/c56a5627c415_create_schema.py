"""create schema

Revision ID: c56a5627c415
Revises: 
Create Date: 2021-05-13 21:43:03.709573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c56a5627c415'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('t_trade',
    sa.Column('asset_class', sa.Text()),
    sa.Column('counterparty', sa.Text()),
    sa.Column('instrument_id', sa.Text()),
    sa.Column('instrument_name', sa.Text()),
    sa.Column('trade_date_time', sa.DateTime(timezone=True), server_default=sa.text('now()')),
    sa.Column('trade_id', sa.Text()),
    sa.Column('trader', sa.Text()),
    sa.PrimaryKeyConstraint('trade_id')
    )
    op.create_table('t_trade_details',
    sa.Column('trade_details_id', sa.Integer(),autoincrement=True),
    sa.Column('trade_id', sa.Text()),
    sa.Column('buysellindicator', sa.Text()),
    sa.Column('price', sa.Numeric()),
    sa.Column('quantity', sa.Integer()),
    sa.PrimaryKeyConstraint('trade_details_id'),
    sa.ForeignKeyConstraint(['trade_id'], ['t_trade.trade_id'], ),
    )


def downgrade():
    op.drop_table('t_trade')
    op.drop_table('t_trade_details')
