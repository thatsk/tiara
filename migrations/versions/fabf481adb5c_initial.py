"""initial

Revision ID: fabf481adb5c
Revises: 
Create Date: 2020-05-02 17:36:18.837724

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'fabf481adb5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('networks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('address', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    op.create_table('ranges',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('network_id', sa.Integer(), nullable=False),
    sa.Column('start', sa.String(length=64), nullable=False),
    sa.Column('stop', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['network_id'], ['networks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ranges_network_id'), 'ranges', ['network_id'], unique=False)
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('range_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('address', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['range_id'], ['ranges.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address')
    )
    op.create_index(op.f('ix_addresses_range_id'), 'addresses', ['range_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_addresses_range_id'), table_name='addresses')
    op.drop_table('addresses')
    op.drop_index(op.f('ix_ranges_network_id'), table_name='ranges')
    op.drop_table('ranges')
    op.drop_table('networks')
    # ### end Alembic commands ###
