"""add foreign key to onboarding

Revision ID: f53c2a7f9204
Revises: 8d3da3b6fb95
Create Date: 2025-05-15 15:54:52.526484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f53c2a7f9204'
down_revision = '8d3da3b6fb95'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_onboardings_employee_id_employees', 'employees', ['employee_id'], ['id'])


def downgrade():
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')