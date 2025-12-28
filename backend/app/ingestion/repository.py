from databases import Database


async def save_cve(db: Database, cve_detail):
    """Insert CVE into DB with related tables"""

    # CVE
    query = """
    INSERT INTO cves (cve_id, source_identifier, published_at, last_modified_at, vuln_status)
    VALUES (:cve_id, :source_identifier, :published_at, :last_modified_at, :vuln_Status)    
    RETURNING id
    """

    cve_id = await db.execute(
        query=query,
        values={
            "cve_id": cve_detail.cve_id,
            "source_identifier": cve_detail.source_identifier,
            "published_at": cve_detail.published_at,
            "last_modified_at": cve_detail.last_modified_at,
            "vuln_status": cve_detail.vuln_status,
        },
    )

    # DESCRIPTION

    query = """
    INSERT INTO cve_description (cve_id, lang, description)
    VALUES (:cve_id, :lang, :description)
    """

    await db.execute(
        query=query,
        values={
            "cve_id": cve_id,
            "lang": cve_id.description.lang,
            "description": cve_id.description.description,
        },
    )

    # CVSS METRICS
    for cvss in cve_detail.cvss_metrics:
        query = """
        INSERT INTO cvss_metrics (cve_id, version, base_score, severity, vector_string, source, type)
        VALUES (:cve_id, :version, :base_score, :severity, :vector_string, :source, :type)
        """
        await db.execute(
            query=query,
            values={
                "cve_id": cve_id,
                "version": cvss.version,
                "base_score": cvss.base_score,
                "severity": cvss.severity,
                "vector_string": cvss.vector_string,
                "source": cvss.source,
                "type": cvss.type,
            },
        )

    return cve_id
