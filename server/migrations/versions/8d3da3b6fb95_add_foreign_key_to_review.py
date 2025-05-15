"""add foreign key to Review

Revision ID: 8d3da3b6fb95
Revises: d77f782e2a1c
Create Date: 2025-05-15 15:37:44.934013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d3da3b6fb95'
down_revision = 'd77f782e2a1c'
branch_labels = None
depends_on = None


def upgrade():
    def upgrade():
     with op.batch_alter_table("reviews") as batch_op:
        batch_op.add_column(sa.Column("employee_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key("fk_reviews_employee_id_employees", "employees", ["employee_id"], ["id"])


def downgrade():
    with op.batch_alter_table("reviews") as batch_op:
        batch_op.drop_constraint("fk_reviews_employee_id_employees", type_="foreignkey")
        batch_op.drop_column("employee_id")
