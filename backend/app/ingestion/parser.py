from app.models.cve import CVEDetail, CVSSMetric, CVEDescription
from datetime import datetime


def parse_cve_item(raw: dict) -> CVEDetail:
    """Normalize a single CVE JSON item to CVEDetail model"""
    cve = raw["cve"]

    descriptions = [
        CVEDescription(lang=d["lang"], description=d["value"])
        for d in cve.get("descriptions", [])
    ]

    cvss_metrics = [
        CVSSMetric(
            version=m["cvssData"]["version"],
            base_score=m["cvssData"].get("baseScore"),
            severity=m["cvssData"].get("baseSeverity"),
            vector_string=m["cvssData"].get("vectorString"),
            source=m.get("source"),
            type=m.get("type"),
        )
        for m in cve.get("metrics", {}).get("cvssMetricV31", [])
    ]

    return CVEDetail(
        cve_id=cve["id"],
        source_identifiers=cve.get("sourceIdentifier"),
        published_at=datetime.fromisoformat(cve["published"])
        if cve.get("published")
        else None,
        last_modified_at=datetime.fromisoformat(cve["lastModified"])
        if cve.get("lastModified")
        else None,
        vuln_status=cve.get("vulnStatus"),
        description=descriptions,
        cvss_metrics=cvss_metrics,
    )
