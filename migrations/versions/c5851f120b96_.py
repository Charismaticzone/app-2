"""empty message

Revision ID: c5851f120b96
Revises: e505cb517589
Create Date: 2019-11-28 23:02:45.781149

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5851f120b96'
down_revision = 'e505cb517589'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('can_use_api_key', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('can_use_custom_domain', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'can_use_custom_domain')
    op.drop_column('users', 'can_use_api_key')
    # ### end Alembic commands ###