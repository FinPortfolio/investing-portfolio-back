"""create ralation between stock and stock transaction

Revision ID: dece643295ed
Revises: b6e8c2044ea3
Create Date: 2025-09-26 09:58:05.582684

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dece643295ed"
down_revision: Union[str, Sequence[str], None] = "b6e8c2044ea3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        "stock_trans",
        "stock_tran_id",
        new_column_name="transaction_id"
    )
    op.add_column(
        "stock_trans",
        sa.Column("symbol_id", sa.String(length=20), nullable=False),
    )
    op.drop_index(
        op.f("ix_stock_trans_stock_tran_id"), table_name="stock_trans"
    )
    op.create_unique_constraint(op.f("uq_stocks_symbol"), "stocks", ["symbol"])
    op.create_foreign_key(
        op.f("fk_stock_trans_symbol_id_stocks"),
        "stock_trans",
        "stocks",
        ["symbol_id"],
        ["symbol"],
    )
    op.alter_column(
        "stocks",
        "symbol",
        existing_type=sa.VARCHAR(length=5),
        type_=sa.String(length=20),
        existing_nullable=False,
    )
    op.alter_column(
        "stocks",
        "name",
        existing_type=sa.VARCHAR(length=50),
        type_=sa.String(length=200),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f("uq_stocks_symbol"), "stocks", type_="unique")
    op.alter_column(
        "stocks",
        "name",
        existing_type=sa.String(length=200),
        type_=sa.VARCHAR(length=50),
        existing_nullable=False,
    )
    op.alter_column(
        "stocks",
        "symbol",
        existing_type=sa.String(length=20),
        type_=sa.VARCHAR(length=5),
        existing_nullable=False,
    )
    op.drop_constraint(
        op.f("fk_stock_trans_symbol_id_stocks"),
        "stock_trans",
        type_="foreignkey",
    )
    op.alter_column(
        "stock_trans",
        "transaction_id",
        new_column_name="stock_tran_id"
    )
    op.drop_column("stock_trans", "symbol_id")
