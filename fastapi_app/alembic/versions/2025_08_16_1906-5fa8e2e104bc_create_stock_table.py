"""create stock table

Revision ID: 5fa8e2e104bc
Revises:
Create Date: 2025-08-16 19:06:52.719208

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "5fa8e2e104bc"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "stocks",
        sa.Column("stock_id", sa.Integer(), nullable=False),
        sa.Column("symbol", sa.String(length=5), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("stock_id", name=op.f("pk_stocks")),
    )


def downgrade() -> None:
    op.drop_table("stocks")
