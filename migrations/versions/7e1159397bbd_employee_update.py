"""employee update

Revision ID: 7e1159397bbd
Revises: 80f8ffa4d7cf
Create Date: 2022-07-25 06:51:18.563580

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e1159397bbd'
down_revision = '80f8ffa4d7cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('name', table_name='employee')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('name', 'employee', ['name'], unique=False)
    # ### end Alembic commands ###
