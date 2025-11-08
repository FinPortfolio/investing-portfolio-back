"""remove server_default from provider

Revision ID: 349834b4687b
Revises: 17fae3873521
Create Date: 2025-11-08 09:25:19.970141

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "349834b4687b"
down_revision: Union[str, Sequence[str], None] = "17fae3873521"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "stocks",
        "provider",
        existing_type=sa.String(length=50),
        nullable=False,
        server_default=None
    )

def downgrade() -> None:
    op.alter_column(
        "stocks",
        "provider",
        existing_type=sa.String(length=50),
        nullable=False,
        server_default="alphavantage"
    )