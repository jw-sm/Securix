from sqlalchemy import insert
from app.db.tables import cves, cve_description, cvss_metrics
from sqlalchemy.engine import Connection


def save_cve(conn: Connection, cve_detail):
    """Insert CVE into DB with related tables"""
    result = conn.execute(
        insert(cves)
        .values(
            cve_id=cve_detail.cve_id,
            source_identifier=cve_detail.source_identifier,
            published_at=cve_detail.published_at,
            last_modified=cve_detail.last_modified,
            vuln_status=cve_detail.vuln_status,
        )
        .returning(cves.c.id)
    )

    cve_id = result.scalar()

    for desc in cve_detail.description:
        conn.execute(
            insert(cve_description).values(
                cve_id=cve_id, lang=desc.lang, description=desc.description
            )
        )

    for cvss in cve_detail.cvss_metrics:
        conn.execute(
            insert(cvss_metrics).values(
                cve_id=cve_id,
                version=cvss.version,
                base_score=cvss.base_score,
                severity=cvss.severity,
                vector_string=cvss.vector_string,
                source=cvss.source,
                type=cvss.type,
            )
        )
