import httpx

NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fetch_cves(params=None) -> dict:
    """Fetch CVEs from NVD and return JSON."""
    response = httpx.get(NVD_API_URL, params=params, timeout=30.0)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    print(f"Fetching {NVD_API_URL}...")
    result = fetch_cves({"startIndex": 20000, "resultsPerPage": 1})
    with open("result.txt", "x") as f:
        f.write(str(result))
    print("Done!")
