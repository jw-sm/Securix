from fastapi import APIRouter, Depends
from app.api.dependencies.database import get_repository
from app.models.cve import CVEDetail
from app.db.repositories.cves import CVERepository

router = APIRouter()


@router.get("/", response_model=list[CVEDetail], name="cves:get-all-cves")
async def get_all_cves(
    cves_repo: CVERepository = Depends(get_repository(CVERepository)),
) -> list[CVEDetail]:
    return await cves_repo.get_all_cves()
