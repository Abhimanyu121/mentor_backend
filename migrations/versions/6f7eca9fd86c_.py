"""empty message

Revision ID: 6f7eca9fd86c
Revises: 7b168592aedd
Create Date: 2019-06-20 12:52:55.881677

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f7eca9fd86c'
down_revision = '7b168592aedd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('mentor', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'mentor')
    # ### end Alembic commands ###
