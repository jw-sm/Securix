from pydantic import BaseModel
from datetime import datetime
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
    version: str
    score: float
    severity: str
    vector: str
    source: str
    type: str
    attack_vector: Optional[str]
    
class CVE(BaseModel):
    cve_id: str
    status: str
    published_at: datetime 
    last_modified_at: datetime 
    description: str
    cvss: Optional[CVEMetric]
    weaknesses: list[str] = []
    references: list[Reference] = []
