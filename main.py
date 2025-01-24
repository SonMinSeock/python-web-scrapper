from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import time

class JobScraper:
    def __init__(self, keywords):
        self.keywords = keywords
    
    def get_page_content(self, url):
        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(url)

        time.sleep(5)

        content = page.content()

        playwright.stop()

        return content

    def scraper_jobs(self, content):
        soup = BeautifulSoup(content, "html.parser")

        jobs = soup.find_all("div", class_="JobCard_container__REty8")

        jobs_db = []

        for job in jobs:
            link = f"https://www.wanted.co.kr/{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__HBpZf").text
            company_name = job.find("span", class_="JobCard_companyName__N1YrF").text
            reward = job.find("span", class_="JobCard_reward__cNlG5").text

            job = {
                "title": title,
                "link": link,
                "company_name": company_name,
                "reward": reward
            }

            jobs_db.append(job)
    
        return jobs_db

    def write_csv(self, keyword, jobs_db):
        file = open(f"{keyword}_jobs.csv", "w")

        writter = csv.writer(file)
        writter.writerow(jobs_db[0].keys())

        for job in jobs_db:
            writter.writerow(job.values())
        
        file.close()

    def run(self):
        for keyword in self.keywords:
            content = self.get_page_content(f"https://www.wanted.co.kr/search?query={keyword}&tab=overview")

            jobs_db = self.scraper_jobs(content)

            self.write_csv(keyword, jobs_db)

keywords = ["react", "nextjs", "typescript", "flutter", "python"]

scraper = JobScraper(keywords)
scraper.run()