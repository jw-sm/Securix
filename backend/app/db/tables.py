from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Float,
    ForeignKey,
    MetaData,
)

metadata = MetaData()

cves = Table(
    "cves",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("cve_id", String(32), nullable=False, unique=True, index=True),
    Column("source_identifier", Text),
    Column("published_at", DateTime),
    Column("last_modified_at", DateTime),
    Column("vuln_status", String(32)),
)

cve_descriptions = Table(
    "cve_descriptions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("cve_id", Integer, ForeignKey("cves.id", ondelete="CASCADE")),
    Column("lang", String(8), nullable=False),
    Column("description", Text, nullable=False),
)

cvss_metrics = Table(
    "cvss_metrics",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("cve_id", Integer, ForeignKey("cves.id", ondelete="CASCADE")),
    Column("version", String(8)),
    Column("base_score", Float),
    Column("severity", String(16)),
    Column("vector_string", Text),
    Column("source", Text),
    Column("type", String(16)),
)
