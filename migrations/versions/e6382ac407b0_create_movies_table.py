"""create movies table

Revision ID: e6382ac407b0
Revises: 19aeeec55b08
Create Date: 2023-12-15 16:31:18.327626

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6382ac407b0'
down_revision: Union[str, None] = '19aeeec55b08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Integer(), nullable=False),
    sa.Column('image', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('reviews', sa.Column('movie_id', sa.Integer(), nullable=True))
    op.add_column('reviews', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reviews', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'reviews', 'movies', ['movie_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_constraint(None, 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'user_id')
    op.drop_column('reviews', 'movie_id')
    op.drop_table('movies')
    # ### end Alembic commands ###