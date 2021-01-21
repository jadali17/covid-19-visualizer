"""empty message

Revision ID: 7782e1b98e83
Revises: 6fbded67ecd8
Create Date: 2021-01-21 14:19:43.040752

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7782e1b98e83'
down_revision = '6fbded67ecd8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('daily', sa.Column('date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('daily', 'date')
    # ### end Alembic commands ###