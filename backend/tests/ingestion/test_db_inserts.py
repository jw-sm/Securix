from sqlalchemy import insert
from app.db.tables import cves


def test_insert_cve(db_conn):
    result = db_conn.execute(
        insert(cves).values(cve_id="CVE-1999-0095").returning(cves.c.id)
    )

    new_id = result.scalar()
    assert new_id is not None
