"""empty message

Revision ID: 92b0937dbde2
Revises: 3877f3dad58b
Create Date: 2020-06-22 17:45:50.278903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92b0937dbde2'
down_revision = '3877f3dad58b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('is_active', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'is_active')
    # ### end Alembic commands ###