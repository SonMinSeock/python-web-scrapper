import requests
from bs4 import BeautifulSoup

keywords = ["flutter", "javascript", "react", "python"]

class Work:
    def __init__(self, url):
        self.url = url
        self.jobs = []

    def scrape_page(self, keyword):
        print(f"Scraping... {self.url}/remote-{keyword}-jobs/")
        response = requests.get(f"{self.url}/remote-{keyword}-jobs", headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        })

        if response.status_code != 200:
            print(f"Error! Unable to fetch data for {keyword}. Status Code: {response.status_code}")
            return
        
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table")
        if not table:
            print("Error! Unable to find job table.")
            return

        jobs = table.find_all("tr", class_="job")
        if not jobs:
            print(f"No jobs found for keyword: {keyword}")
            return

        for job in jobs:
            company_name = job.find("span", class_="companyLink")
            link = job.find("a", class_="preventLink")
            
            if not company_name or not link:
                print("Error! Missing data in job posting.")
                continue
            
            job_link = link["href"]
            if not job_link.startswith("http"):
                job_link = f"{self.url}/{job_link}"
            
            self.jobs.append({
                "keyword": keyword,
                "company_name": company_name.text.strip(),
                "link": job_link
            })

        print(f"Found {len(self.jobs)} jobs for keyword: {keyword}")

work = Work("https://remoteok.com")

for keyword in keywords:
    work.scrape_page(keyword)

print(work.jobs)
