"""mp_notice

Revision ID: cf266bf19ef3
Revises: 49b4f1838f35
Create Date: 2019-05-04 22:42:02.845137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf266bf19ef3'
down_revision = '49b4f1838f35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likecomment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.String(length=32), nullable=True),
    sa.Column('time', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['article1.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['role1.uuid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('role1', sa.Column('last_reply_read_time', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role1', 'last_reply_read_time')
    op.drop_table('likecomment')
    # ### end Alembic commands ###
