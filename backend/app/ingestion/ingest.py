from app.db.tasks import create_database
from app.ingestion.parser import parse_nvd
from app.ingestion.fetch import fetch_cves
from app.ingestion.repository import save_cve
import logging
import asyncio

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def run_ingestion(db, start_index=132000):
    logger.info("Starting CVE ingestion...")

    raw_data = fetch_cves({"startIndex": start_index})
    items = raw_data.get("vulnerabilities", [])
    if not items:
        logger.info("No CVEs to ingest.")
        return

    success_count = 0
    fail_count = 0

    async with db.transaction():
        for item in items:
            try:
                cve_detail = parse_nvd(item)
                await save_cve(db, cve_detail)
                success_count += 1
                logger.info(f"Ingested CVE: {cve_detail.cve_id}")
            except Exception as e:
                fail_count += 1
                logger.error(f"Failed to ingest CVE: {item.get('cve', {}).get('id', 'UNKNOWN')}. Error: {e}")

    logger.info(f"Batch ingestion completed: {success_count} succeeded, {fail_count} failed.")


async def main():
    db = create_database()
    await db.connect()

    try:
        await run_ingestion(db)
    finally:
        await db.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

