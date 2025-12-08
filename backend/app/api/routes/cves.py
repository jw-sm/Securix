from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_all_cves() -> list[dict]:
    cves = [
        {
            "resultsPerPage": 2,
            "startIndex": 0,
            "totalResults": 3049,
            "format": "CVE_FEED",
            "version": "1.0",
            "timestamp": "2025-11-21T20:00:01Z",
            "vulnerabilities": [
                {
                    "cve": {
                        "id": "CVE-2011-2462",
                        "published": "2011-12-07T19:55:01Z",
                        "lastModified": "2025-11-21T16:16:00Z",
                        "descriptions": [
                            {
                                "lang": "en",
                                "value": "Unspecified vulnerability in Adobe Reader and Acrobat...",
                            }
                        ],
                        "metrics": {
                            "cvssV31": {
                                "baseScore": 9.8,
                                "severity": "CRITICAL",
                                "vector": "AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                            }
                        },
                        "weaknesses": [{"cwe": "CWE-787"}],
                        "configurations": [
                            {
                                "vendor": "Adobe",
                                "product": "Acrobat Reader",
                                "affectedVersions": "<= 10.1.1",
                            }
                        ],
                        "references": [
                            {
                                "url": "http://www.adobe.com/support/security/advisories/apsa11-04.html",
                                "tags": ["Vendor Advisory"],
                            }
                        ],
                    }
                },
                {
                    "cve": {
                        "id": "CVE-2012-0754",
                        "published": "2012-02-16T19:55:01Z",
                        "lastModified": "2025-11-17T21:15:44Z",
                        "descriptions": [
                            {
                                "lang": "en",
                                "value": "Adobe Flash Player before 10.3.183.15 ...",
                            }
                        ],
                        "metrics": {
                            "cvssV31": {
                                "baseScore": 8.1,
                                "severity": "HIGH",
                                "vector": "AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H",
                            }
                        },
                        "weaknesses": [{"cwe": "CWE-787"}],
                        "configurations": [
                            {
                                "vendor": "Adobe",
                                "product": "Flash Player",
                                "affectedVersions": "< 11.1.102.62",
                            }
                        ],
                        "references": [
                            {
                                "url": "https://www.adobe.com/support/security/bulletins/apsb12-03.html",
                                "tags": ["Vendor Advisory", "Patch"],
                            }
                        ],
                    }
                },
            ],
        }
    ]

    return cves
