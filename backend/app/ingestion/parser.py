from app.models.cve import CVEDetail, CVSSMetric, CVEDescription
from datetime import datetime
from app.ingestion.fetch import fetch_cves
import json
import ast

def parse_cve_item(raw: dict) -> CVEDetail:
    """Normalize a single CVE JSON item to CVEDetail model"""
    cve = raw.get["cve"]
    if not cve:
        raise ValueError("Invalid CVE item: missing 'cve'")

    descriptions = [
        CVEDescription(lang=d["lang"], description=d["value"])
        for d in cve.get("descriptions", [])
    ]

    """
    cvss_metrics = [
        CVSSMetric(
            version=m["cvssData"]["version"],
            base_score=m["cvssData"].get("baseScore"),
            severity=m.get("baseSeverity"),
            vector_string=m["cvssData"].get("vectorString"),
            source=m.get("source"),
            type=m.get("type"),
        )
        for m in cve.get("metrics", {}).get("cvssMetricV31", [])
    ]
    """
    cvss_metrics = []
    metrics = cve.get("metrics", {})
    for key in ("cvssMetricV31", "cvssMetricV30", "cvssMetricV2"):
        for m in metrics.get(key, []):
            cvss_metrics.append(
                CVSSMetric(
                    version=m["cvssData"].get("version"),
                    base_score=m["cvssData"].get("baseScore"),
                    severity=m.get("baseSeverity"),
                    vector_string=m["cvssData"].get("vectorString"),
                    source=m.get("source"),
                    type=m.get("type"),
                )
            )

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

if __name__ == "__main__":
    # data is currently single-quoted JSON file, which is like a python object
    # read it with ast.literal_eval before using json.dumps unless data changes
    with open("result.txt") as f:
        data = ast.literal_eval(f.read())

    json_text = json.dumps(data)
    print(json_text)
        
