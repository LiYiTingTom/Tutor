"""empty message

Revision ID: 5a9562895ca9
Revises: e4b26190e602
Create Date: 2021-04-25 15:38:07.913516

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a9562895ca9'
down_revision = 'e4b26190e602'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('set', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'set')
    # ### end Alembic commands ###