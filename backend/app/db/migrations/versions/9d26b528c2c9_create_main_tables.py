"""create_cve_tables

Revision ID: a1b2c3d4e5f6
Revises:
Create Date: 2025-12-16
"""

from alembic import op
import sqlalchemy as sa

revision = "a1b2c3d4e5f6"
down_revision = None
branch_labels = None
depends_on = None


def create_cves_table():
    op.create_table(
        "cves",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("cve_id", sa.String(32), nullable=False, unique=True, index=True),
        sa.Column("source_identifier", sa.Text),
        sa.Column("published_at", sa.DateTime),
        sa.Column("last_modified_at", sa.DateTime),
        sa.Column("vuln_status", sa.String(32)),
    )


def create_descriptions_table():
    op.create_table(
        "cve_descriptions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("cve_id", sa.Integer, sa.ForeignKey("cves.id", ondelete="CASCADE")),
        sa.Column("lang", sa.String(8), nullable=False),
        sa.Column("description", sa.Text, nullable=False),
    )


def create_cvss_table():
    op.create_table(
        "cvss_metrics",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("cve_id", sa.Integer, sa.ForeignKey("cves.id", ondelete="CASCADE")),
        sa.Column("version", sa.String(8)),
        sa.Column("base_score", sa.Float),
        sa.Column("severity", sa.String(16)),
        sa.Column("vector_string", sa.Text),
        sa.Column("source", sa.Text),
        sa.Column("type", sa.String(16)),
    )


def upgrade():
    create_cves_table()
    create_descriptions_table()
    create_cvss_table()


def downgrade():
    op.drop_table("cvss_metrics")
    op.drop_table("cve_descriptions")
    op.drop_table("cves")

