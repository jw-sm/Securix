from sqlalchemy import insert
from app.ingestion.parser import parse_cve_item
from app.ingestion.repository import save_cve
import ast


def test_insert_cve(db_conn):
    """
    result = db_conn.execute(
        insert(cves).values(cve_id="CVE-1999-0095").returning(cves.c.id)
    )
    """
    with open("result.txt") as f:
        data = ast.literal_eval(f.read())
    vuln = data.get("vulnerabilities", [])
    cve = parse_cve_item(vuln[0])

    result = save_cve(db_conn, cve)
    assert result is not None
