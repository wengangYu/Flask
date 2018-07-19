"""empty message

Revision ID: a3f61e02f663
Revises: 
Create Date: 2018-07-19 16:42:23.245154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3f61e02f663'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sign', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('shop_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sign', sa.Integer(), nullable=True),
    sa.Column('shop_name', sa.String(length=32), nullable=True),
    sa.Column('start_cost', sa.Float(), nullable=True),
    sa.Column('shipping_fee', sa.Float(), nullable=True),
    sa.Column('shop_notice', sa.String(length=128), nullable=True),
    sa.Column('discounts', sa.String(length=128), nullable=True),
    sa.Column('is_brand', sa.Boolean(), nullable=True),
    sa.Column('is_ontime', sa.Boolean(), nullable=True),
    sa.Column('is_bird', sa.Boolean(), nullable=True),
    sa.Column('is_bao', sa.Boolean(), nullable=True),
    sa.Column('is_fp', sa.Boolean(), nullable=True),
    sa.Column('is_zun', sa.Boolean(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('shop_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_info')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
