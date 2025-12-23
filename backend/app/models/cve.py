from datetime import datetime
from app.models.core import CoreModel, IDModelMixin


class CVE(CoreModel):
    cve_id: str
    vuln_status: str


class CVEWithID(IDModelMixin, CVE):
    pass


class CVESearchResponse(CoreModel):
    total_results: int
    results_per_page: int
    start_index: int
    items: list[CVEWithID]


class CVEDescription(CoreModel):
    lang: str
    description: str


class CVSSMetric(CoreModel):
    version: str
    base_score: float | None
    severity: str | None
    vector_string: str | None
    source: str | None
    type: str | None


# Full CVE response
class CVEDetail(CoreModel):
    cve_id: str
    source_identifiers: list[str] | None
    published_at: datetime | None
    last_modified_at: datetime | None
    vuln_status: str

    descriptions: list[CVEDescription]
    cvss_metrics: list[CVSSMetric]
