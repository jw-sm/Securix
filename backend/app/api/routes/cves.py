from fastapi import APIRouter, Depends, Path, HTTPException
from app.api.dependencies.database import get_repository
from app.models.cve import CVEDetail
from app.db.repositories.cves import CVERepository

from starlette.status import HTTP_404_NOT_FOUND

router = APIRouter()

@router.get("/{cve_id_query}", response_model=CVEDetail, name="cves:get_cve_by_id")
async def get_cve_by_id(
    cve_id_query: str = Path(required=True, title="CVE to get"),
    cve_repo = CVERepository = Depends(get_repository(CVERepository))
) -> CVEDetail:
    cve = await cve_repo.get_cve_by_id(cve_id_query=cve_id_query)
    if not cve:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="No cve id found")
    return cve
