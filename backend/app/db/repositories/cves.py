from app.db.respositories.base import BaseRepository
from app.models.cve import CVEDetail


class CVERepository(BaseRepository):
    """
    All database actions associated with the CVE resources
    """

    async def get_all_cves(self) -> list[CVEDetail]:
        GET_ALL_CVES_QUERY = """
            SELECT cve_id, source_identifiers, published_at, last_modified_at, vuln_status, descriptions, cvss_metrics
            FROM cves;
        """
        cve_records = await self.db.fetch_all(query=GET_ALL_CVES_QUERY)
        return [CVEDetail(**cve) for cve in cve_records]
