"""empty message

Revision ID: 3d0a70598801
Revises: 4f5885c51237
Create Date: 2021-01-21 15:41:34.966159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d0a70598801'
down_revision = '4f5885c51237'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('daily', sa.Column('daily_cases', sa.Integer(), nullable=True))
    op.add_column('daily', sa.Column('daily_deaths', sa.Integer(), nullable=True))
    op.add_column('daily', sa.Column('daily_recoveries', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('daily', 'daily_recoveries')
    op.drop_column('daily', 'daily_deaths')
    op.drop_column('daily', 'daily_cases')
    # ### end Alembic commands ###
