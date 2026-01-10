import ast
from app.models.cve import CVE, CVEMetric, Reference

def parse_nvd(item: dict) -> CVE:
    cve_data = item["cve"]

    # prioritize English, fallback to "No description" if none.
    description = next((d["value"] for d in cve_data.get("descriptions", []) if d["lang"] == "en"), "No description")

    # CVSS Metric
    cvss_data = None
    for metric_key in ["cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2", "cvssMetricV1"]:
        metrics = cve_data.get("metrics", {}).get(metric_key, [])
        if metrics:
            cvss_info = metrics[0]["cvssData"]
            cvss_data = CVEMetric(
                source=metrics[0].get("source", ""), 
                type=metrics[0].get("type", ""),
                version=cvss_info.get("version", ""),
                score=cvss_info.get("baseScore", 0.0),
                severity=metrics[0].get("baseSeverity", "Unknown"),
                vector=cvss_info.get("vectorString", ""),
                attack_vector=cvss_info.get("attackVector")
            )
            break

    # Weaknesses
    weaknesses = [
        w_desc["value"]
        for w in cve_data.get("weaknesses", [])
        for w_desc in w.get("description", [])
        if w_desc["lang"] == "en"
    ]
        
    # Reference
    reference = [
        Reference(
            url=ref["url"],
            source=ref["source"],
        )
        for ref in cve_data.get("references", [])
    ]

    c = CVE(
        cve_id=cve_data.get("id", ""),
        status=cve_data.get("vulnStatus", ""),
        published_at=cve_data.get("published", ""),
        last_modified_at=cve_data.get("lastModified", ""),
        description=description,
        cvss=cvss_data,
        weaknesses=weaknesses,
        references=reference,
    )
    return c

                
if __name__ == "__main__":
    # data is currently single-quoted JSON file, which is like a python object
    with open("result.txt") as f:
        data = ast.literal_eval(f.read())
        vulns = data.get("vulnerabilities", [])
        
    for vul in vulns:
        v = parse_nvd(vul)
        breakpoint()
