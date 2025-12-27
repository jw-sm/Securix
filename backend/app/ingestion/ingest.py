import logging

from ingestion.fetch import fetch_cves
from ingestion.parser import parse_cve_item
from ingestion.repository import save_cve
from ingestion.session import get_connection

logger = logging.getLogger(__name__)


def run_ingestion():
    logger.info("Starting CVE ingestion")

    raw_data = fetch_cves()

    items = raw_data.get("vulnerabilities", [])

    with get_connection as conn:
        for item in items:
            cve_detail = parse_cve_item(item)
            save_cve(conn, cve_detail)

    logger.info(f"ingested {len(items)} CVEs successfully.")


if __name__ == "__main__":
    run_ingestion()
