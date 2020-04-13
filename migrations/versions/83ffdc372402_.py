"""empty message

Revision ID: 83ffdc372402
Revises: 
Create Date: 2020-04-14 06:26:50.646909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83ffdc372402'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('rides',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('wheelchair', sa.Boolean(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedule_stops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('schedule_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=8, scale=5), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=8, scale=5), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedules.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('schedule_stop_rides',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('schedule_stop_id', sa.Integer(), nullable=True),
    sa.Column('ride_id', sa.Integer(), nullable=True),
    sa.Column('stop_type', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['ride_id'], ['rides.id'], ),
    sa.ForeignKeyConstraint(['schedule_stop_id'], ['schedule_stops.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule_stop_rides')
    op.drop_table('schedule_stops')
    op.drop_table('rides')
    op.drop_table('users')
    op.drop_table('schedules')
    # ### end Alembic commands ###
