from alembic import op
import sqlalchemy as sa

revision = "b2c3d4e5f6g7"
down_revision = None
branch_labels = None
depends_on = None

def create_cves_table():
    op.create_table(
        "cves",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("cve_id", sa.String(32), nullable=False, unique=True, index=True),
        sa.Column("status", sa.String(32)),
        sa.Column("published_at", sa.DateTime),
        sa.Column("last_modified_at", sa.DateTime),
        sa.Column("description", sa.Text),
    )


def create_cvss_table():
    op.create_table(
        "cvss_metrics",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "cve_id",
            sa.String(32),
            sa.ForeignKey("cves.cve_id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("version", sa.String(8)),
        sa.Column("base_score", sa.Float),
        sa.Column("severity", sa.String(16)),
        sa.Column("vector_string", sa.Text),
        sa.Column("attack_vector", sa.String(32)),
        sa.Column("source", sa.Text),
        sa.Column("type", sa.String(16)),
    )


def create_descriptions_table():
    op.create_table(
        "cve_descriptions",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "cve_id",
            sa.String(32),
            sa.ForeignKey("cves.cve_id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("lang", sa.String(8), nullable=False),
        sa.Column("description", sa.Text, nullable=False),
    )


def create_weaknesses_table():
    op.create_table(
        "cve_weaknesses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "cve_id",
            sa.String(32),
            sa.ForeignKey("cves.cve_id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("cwe_id", sa.String(16), nullable=False),
        sa.Column("description", sa.Text),
    )


"""
def create_affected_products_table():
    op.create_table(
        "cve_affected_products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "cve_id",
            sa.String(32),
            sa.ForeignKey("cves.cve_id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("vendor", sa.String(64)),
        sa.Column("product", sa.String(64)),
        sa.Column("version_start", sa.String(32)),
        sa.Column("version_end_excluding", sa.String(32)),
    )
"""


def create_references_table():
    op.create_table(
        "cve_references",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "cve_id",
            sa.String(32),
            sa.ForeignKey("cves.cve_id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("url", sa.Text, nullable=False),
        sa.Column("type", sa.String(32)),
    )


def upgrade():
    create_cves_table()
    create_cvss_table()
    create_descriptions_table()
    create_weaknesses_table()
   #create_affected_products_table()
    create_references_table()


def downgrade():
    op.drop_table("cve_references")
    #op.drop_table("cve_affected_products")
    op.drop_table("cve_weaknesses")
    op.drop_table("cve_descriptions")
    op.drop_table("cvss_metrics")
    op.drop_table("cves")
