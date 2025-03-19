import requests
from bs4 import BeautifulSoup

def scrape_jobs(skill):
    jobs = []
    indeed_url = f"https://www.indeed.com/jobs?q={skill}&l=remote"
    response = requests.get(indeed_url)
    soup = BeautifulSoup(response.text, "html.parser")

    for job_card in soup.find_all("div", class_="job_seen_beacon"):
        title = job_card.find("h2").text.strip()
        company = job_card.find("span", class_="companyName").text.strip()
        location = job_card.find("div", class_="companyLocation").text.strip()
        apply_link = "https://www.indeed.com" + job_card.find("a")["href"]

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "apply_link": apply_link
        })

    return jobs
