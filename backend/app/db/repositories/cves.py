from app.db.repositories.base import BaseRepository
from app.models.cve import CVE
import json

class CVERepository(BaseRepository):
    async def get_cve_by_id(self, cve_id: str) -> CVE | None:
    # this will work for now, but we can change the schemas' FK to id probably???
        query = """
    SELECT
        c.id,
        c.cve_id,
        c.published_at,
        c.last_modified_at,
        c.source_identifier,
        c.vuln_status,

        -- first description as JSON object
        (
            SELECT jsonb_build_object(
                'lang', d.lang,
                'description', d.description
            )
            FROM cve_descriptions d
            WHERE d.cve_id = c.cve_id
            ORDER BY d.id
            LIMIT 1
        ) AS description,

        -- all descriptions as JSONB array
        (
            SELECT coalesce(jsonb_agg(jsonb_build_object(
                'lang', d.lang,
                'description', d.description
            ) ORDER BY d.id), '[]'::jsonb)
            FROM cve_descriptions d
            WHERE d.cve_id = c.cve_id
        ) AS descriptions,

        -- all CVSS metrics as JSONB array
        (
            SELECT coalesce(jsonb_agg(m ORDER BY m.id), '[]'::jsonb)
            FROM cvss_metrics m
            WHERE m.cve_id = c.cve_id
        ) AS cvss_metrics

    FROM cves c
    WHERE c.cve_id = :cve_id;
    """
        cve_record = await self.db.fetch_one(query=query, values={"cve_id": cve_id})

        if not cve_record:
            return None

        cve = dict(cve_record)

        if cve.get("description") and isinstance(cve["description"], str):
            cve["description"] = json.loads(cve["description"])

        if cve.get("descriptions") and isinstance(cve["descriptions"], str):
            cve["descriptions"] = json.loads(cve["descriptions"])

        if cve.get("cvss_metrics") and isinstance(cve["cvss_metrics"], str):
            cve["cvss_metrics"] = json.loads(cve["cvss_metrics"])

        return CVEDetail(**cve)

