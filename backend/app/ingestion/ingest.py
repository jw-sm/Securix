from app.db.tasks import create_database
from app.ingestion.parser import parse_cve_item
from app.ingestion.fetch import fetch_cves
from app.ingestion.repository import save_cve
import logging

logger = logging.getLogger(__name__)

async def run_ingestion(db):
    logger.info("Starting CVE ingestion...")
    
    raw_data = fetch_cves()
    items = raw_data.get("vulnerabilities", [])
    
    for item in items:
        cve_detail = parse_cve_item(item)
        await save_cve(db, cve_detail)

    logger.info(f"Ingested {len{items}} CVEs successfully.")


async def main():
    db = create_database()
    await db.connect()

    try:
        await run_ingestion(db)
    finally:
        await db.disconnect()
