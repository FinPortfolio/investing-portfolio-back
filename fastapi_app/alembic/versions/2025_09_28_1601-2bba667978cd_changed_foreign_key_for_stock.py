"""changed foreign key for stock

Revision ID: 2bba667978cd
Revises: dece643295ed
Create Date: 2025-09-28 16:01:21.696178

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2bba667978cd"
down_revision: Union[str, Sequence[str], None] = "dece643295ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "stock_trans", sa.Column("asset_id", sa.Integer(), nullable=True)
    )

    connection = op.get_bind()
    connection.execute(sa.text("""
        UPDATE stock_trans
        SET asset_id = s.stock_id
        FROM stocks s
        WHERE stock_trans.symbol_id = s.symbol
    """))

    op.alter_column("stock_trans", "asset_id", nullable=False)
    op.add_column(
        "stock_trans",
        sa.Column("provider", sa.String(length=50), nullable=False, server_default="Unknown"),
    )
    op.alter_column("stock_trans", "provider", server_default=None)
    op.drop_constraint(
        op.f("fk_stock_trans_symbol_id_stocks"),
        "stock_trans",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_stock_trans_asset_id_stocks"),
        "stock_trans",
        "stocks",
        ["asset_id"],
        ["stock_id"],
    )
    op.drop_column("stock_trans", "symbol_id")


def downgrade() -> None:
    """Downgrade schema safely."""
    op.add_column(
        "stock_trans",
        sa.Column("symbol_id", sa.VARCHAR(length=20), nullable=True),
    )

    connection = op.get_bind()
    connection.execute(sa.text("""
        UPDATE stock_trans
        SET symbol_id = s.symbol
        FROM stocks s
        WHERE stock_trans.asset_id = s.stock_id
    """))

    op.alter_column("stock_trans", "symbol_id", nullable=False)

    op.drop_constraint(
        op.f("fk_stock_trans_asset_id_stocks"),
        "stock_trans",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_stock_trans_symbol_id_stocks"),
        "stock_trans",
        "stocks",
        ["symbol_id"],
        ["symbol"],
    )

    op.drop_column("stock_trans", "provider")
    op.drop_column("stock_trans", "asset_id")
