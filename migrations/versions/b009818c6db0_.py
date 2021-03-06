"""empty message

Revision ID: b009818c6db0
Revises: 6041d08f0f23
Create Date: 2020-06-25 16:30:03.196989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b009818c6db0'
down_revision = '6041d08f0f23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('employers_ibfk_1', 'employers', type_='foreignkey')
    op.create_foreign_key(None, 'employers', 'adress', ['fk_adress_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employers', type_='foreignkey')
    op.create_foreign_key('employers_ibfk_1', 'employers', 'adress', ['fk_adress_id'], ['id'])
    # ### end Alembic commands ###
