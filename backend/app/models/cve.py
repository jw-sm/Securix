from pydantic import BaseModel
from typing import Optional

class Reference(BaseModel):
    url: str
    source: str

""" to be added soon
class AffectedProducts(BaseModel):
    vendor: str
    product: str
    version_start: Optional[str]
    version_end_excluding: Optional[str]
"""

class CVEMetric(BaseModel):
    score: float
    severity: str
    vector: str
    attack_vector: Optional[str]
    
class CVE(BaseModel):
    cve_id: str
    status: str
    published: str
    last_modified: str
    description: str
    cvss: Optional[CVEMetric]
    weaknesses: list[str] = []
    references: list[Reference] = []
