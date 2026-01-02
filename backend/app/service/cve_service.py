from app.core.errors import RecordNotFoundError
from app.core.exceptions import CVENotFoundError
from app.api.dependencies.database import get_repository
from app.db.repositories.cves import CVERepository

from fastapi import Depends

class CVEService:
    def __init__(
        self, repo: CVERepository = Depends(get_repository(CVERepository))
    ) -> CVERepository:
        self.repo = repo

    async def get_cve_by_id(self, cve_id: str) -> CVEDetail:
        try:
            cve = await self.repo.get_cve_by_id(cve_id)
        except RecordNotFoundError as exc:
            raise CVENotFoundError("No CVE with that ID exists") from exc
        return cve
