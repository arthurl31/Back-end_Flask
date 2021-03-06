"""empty message

Revision ID: aa35a3d5f616
Revises: 5387cf75f5a9
Create Date: 2020-05-27 20:47:08.930923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa35a3d5f616'
down_revision = '5387cf75f5a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('list_product_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fk_order_id', sa.Integer(), nullable=True),
    sa.Column('fk_product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['fk_product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('list_product_order')
    # ### end Alembic commands ###
