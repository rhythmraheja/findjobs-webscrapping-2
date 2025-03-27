import requests
from bs4 import BeautifulSoup
import requests
import os

def scrape_jobs(skill):
    jobs = []
    api_key = os.getenv("SERPAPI_KEY")  # Load API key from environment variables

    if not api_key:
        raise ValueError("SERPAPI_KEY is not set. Please configure your API key.")

    params = {
        "engine": "google_jobs",
        "q": skill,  # No site restriction → fetch from all sources
        "hl": "en",
        "api_key": api_key
    }

    response = requests.get("https://serpapi.com/search", params=params)
    
    if response.status_code == 200:
        data = response.json()
        if "jobs_results" in data:
            for job in data["jobs_results"]:
                jobs.append({
                    "title": job.get("title", "N/A"),
                    "company": job.get("company_name", "N/A"),
                    "location": job.get("location", "N/A"),
                    "source": job.get("detected_extensions", {}).get("source", "Unknown"),
                    "apply_link": (job.get("apply_options") or [{}])[0].get("link", "N/A")
                })
    else:
        print("Error:", response.status_code, response.text)

    return jobs