from app.db.repositories.base import BaseRepository
from app.models.cve import CVEDetail

class CVERepository(BaseRepository):
    """
    All database actions associated with the CVE resources
    """
    async def get_cve_by_id(self, *, cve_id: str) -> CVEDetail:
        query="""
        SELECT
            c.id,
            c.cve_id,
            c.published_at,
            c.last_modified_at,
        
            COALESCE(d.descriptions, '[]'::json) AS descriptions
            COALESCE(m.cvss_metrics, '[]'::json) AS cvss_metrics

        FROM cves c

        LEFT JOIN LATERAL (
            SELECT json_agg(d ORDER BY d.id) AS descriptions
            FROM cve_descriptions d
            WHERE d.cve_id = c.id
        ) d ON TRUE

        LEFT JOIN LATERAL (
            SELECT json_agg(m ORDER BY m.id) AS cvss_metrics
            FROM cvss_metrics m
            WHERE m.cve_id = c.id
        ) m ON TRUE

        WHERE c.cve_id = :cve_id
        """

        cve = await self.db.fetch_one(query=query, values={"cve_id": cve_id})
        if not cve:
            return None
        return CVEDetail(**cve)

