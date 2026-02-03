"""create employees and attendance

Revision ID: de4fbdd98108
Revises: 
Create Date: 2026-02-02 18:10:17.537948
"""

from alembic import op
import sqlalchemy as sa


revision = 'de4fbdd98108'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
   
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.String(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('department', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('employee_id')
    )
    op.create_table('attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
   


def downgrade():
    
    op.drop_table('attendance')
    op.drop_table('employees')
   
