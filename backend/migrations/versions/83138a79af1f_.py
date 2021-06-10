"""empty message

Revision ID: 83138a79af1f
Revises: df8fa844f473
Create Date: 2021-06-10 00:07:58.870219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83138a79af1f'
down_revision = 'df8fa844f473'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favorite', 'vacancy_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('favorite', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite', sa.Column('id', sa.INTEGER(), nullable=False))
    op.alter_column('favorite', 'vacancy_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###