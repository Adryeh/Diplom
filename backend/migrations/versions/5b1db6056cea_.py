"""empty message

Revision ID: 5b1db6056cea
Revises: 7d02e456ac7b
Create Date: 2021-06-10 17:55:35.993587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b1db6056cea'
down_revision = '7d02e456ac7b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorite', sa.Column('id', sa.Integer(), nullable=False))
    op.alter_column('favorite', 'vacancy_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('favorite', 'vacancy_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('favorite', 'id')
    # ### end Alembic commands ###
