from databases import Database


async def save_cve(db: Database, cve_detail):
    """Insert CVE into DB with related tables"""

    # CVE
    query = """
    INSERT INTO cves (cve_id, status, published_at, last_modified_at, description)
    VALUES (:cve_id, :status, :published_at, :last_modified_at, :description)    
    ON CONFLICT (cve_id) DO UPDATE
    SET status = EXCLUDED.status,
        published_at = EXCLUDED.published_at,
        last_modified_at = EXCLUDED.last_modified_at,
        description = EXCLUDED.description
    RETURNING id
    """

    cve_id = await db.execute(
        query=query,
        values={
            "cve_id": cve_detail.cve_id,
            "status": cve_detail.status,
            "published_at": cve_detail.published_at,
            "last_modified_at": cve_detail.last_modified_at,
            "description": cve_detail.description,
        },
    )

    # DESCRIPTION
    query = """
    INSERT INTO cve_descriptions (cve_id, description)
    VALUES (:cve_id, :description)
    """
    await db.execute(
        query=query,
        values={
            "cve_id": cve_detail.cve_id,
            "description": cve_detail.description,
        },
    )

    # CVSS METRICS
    cvss = cve_detail.cvss
    assert cvss is not None
    query = """
    INSERT INTO cvss_metrics (cve_id, version, base_score, severity, vector_string, source, type)
    VALUES (:cve_id, :version, :base_score, :severity, :vector_string, :source, :type)
    """
    await db.execute(
        query=query,
        values={
            "cve_id": cve_detail.cve_id,
            "version": cvss.version,
            "base_score": cvss.score,
            "severity": cvss.severity,
            "vector_string": cvss.vector,
            "source": cvss.source,
            "type": cvss.type,
        },
    )
    return cve_id
