from app.db.tasks import create_database
from app.ingestion.parser import parse_nvd
from app.ingestion.fetch import fetch_cves
from app.ingestion.repository import save_cve
import logging
import asyncio

logger = logging.getLogger(__name__)


async def run_ingestion(db):
    logger.info("Starting CVE ingestion...")

    raw_data = fetch_cves({"startIndex": 20000, "resultsPerPage": 1})
    items = raw_data.get("vulnerabilities", [])

    for item in items:
        cve_detail = parse_nvd(item)
        await save_cve(db, cve_detail)

    logger.info(f"Ingested {len(item)} CVEs successfully.")


async def main():
    db = create_database()
    await db.connect()

    try:
        await run_ingestion(db)
    finally:
        await db.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
