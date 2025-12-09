from fastapi import APIRouter

from app.api.routes.cves import router as cves_router

router = APIRouter()

router.include_router(cves_router, prefix="/cves", tags=["cves"])
