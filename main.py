from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/search?query=flutter&tab=overview")

# time.sleep(5)

# page.click("button.Aside_searchButton__rajGo")
# # page.locator("button.Aside_searchButton__rajGo").click()

# time.sleep(5)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

# page.click("a#search_tab_position")

# time.sleep(5)

# for x in range(5):
#     page.keyboard.down("End")
#     time.sleep(5)


content = page.content()

playwright.stop()

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


print(jobs_db)
print(len(jobs_db))