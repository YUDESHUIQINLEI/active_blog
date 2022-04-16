"""empty message

Revision ID: 5abb11932367
Revises: c64451eedb8e
Create Date: 2022-04-15 21:36:20.633450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5abb11932367'
down_revision = 'c64451eedb8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###
