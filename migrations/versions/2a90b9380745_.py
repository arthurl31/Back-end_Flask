"""empty message

Revision ID: 2a90b9380745
Revises: 
Create Date: 2020-05-21 23:23:57.723473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a90b9380745'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('entry_date', sa.Date(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('is_super', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('total_value', sa.Float(), nullable=False),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('fk_client_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=100), nullable=False),
    sa.Column('product_value', sa.Float(), nullable=False),
    sa.Column('available_quantity', sa.Integer(), nullable=False),
    sa.Column('add_by', sa.Integer(), nullable=True),
    sa.Column('add_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['add_by'], ['employers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('orders')
    op.drop_table('employers')
    op.drop_table('clients')
    # ### end Alembic commands ###
