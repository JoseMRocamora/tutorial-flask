"""Añade campo created a Post

Revision ID: 23794a5c0fac
Revises: d75c12f04ffb
Create Date: 2020-08-07 13:23:45.380150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23794a5c0fac'
down_revision = 'd75c12f04ffb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('created', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'created')
    # ### end Alembic commands ###
