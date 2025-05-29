"""Merge three heads

Revision ID: 1d37e788e9dc
Revises: 15ab35cae29f, 6f5c94cf2f46, bbd0f725fc27
Create Date: 2025-05-29 17:08:50.272738

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d37e788e9dc'
down_revision: Union[str, None] = ('15ab35cae29f', '6f5c94cf2f46', 'bbd0f725fc27')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
