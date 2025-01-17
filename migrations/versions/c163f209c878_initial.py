"""Initial

Revision ID: c163f209c878
Revises: 
Create Date: 2024-05-04 12:10:25.489501

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c163f209c878'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Tasks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=75), nullable=False),
    sa.Column('task', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Tasks')
    # ### end Alembic commands ###
