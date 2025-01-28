# BLUEPRINT | DONT EDIT

import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://berlinstartupjobs.com/engineering/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

skills = ["python", "typescript", "javascript", "rust"]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE
job_enginer_db = []
job_db = {}

def getPages(page_content):
    if not page_content:
        print("URL 페이지네이션 할 URL이 없습니다!")
        return
    else:
        soup = BeautifulSoup(page_content, "html.parser")
        pages = soup.select(".page-numbers")
        return len(pages) - 1

pages = getPages(response.content)

def scraper_enginer(url, page):
    # https://berlinstartupjobs.com/engineering/page/2 -> 두 번째 페이지
    response = requests.get(
        f"{url}/engineering/page/{page}",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
    
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")
    
    for job in jobs:
        title = job.find("h4", class_="bjs-jlid__h").text
        job_type = job.find("a", class_="bjs-jlid__b").text
        link = job.find("a", class_="bjs-jlid__b")["href"]
        
        decription = job.find("div", class_="bjs-jlid__description").text
       
        job_data = {
            "title": title,
            "job_type": job_type,
            "decription": decription,
            "link": link
        }

        job_enginer_db.append(job_data)

def scraper_job(url, keyword):
    response = requests.get(
        f"{url}/skill-areas/{keyword}",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    jobs = soup.find("ul", class_="jobs-list-items").find_all("div", class_="bjs-jlid__wrapper")

    for job in jobs:
        company_name_element = job.find("a", class_="bjs-jlid__b")
        
        company_name = company_name_element.text
        job_title = job.find("h4", class_="bjs-jlid__h").text
        link = company_name_element["href"]
        decription = job.find("div", class_="bjs-jlid__description").text
    
       
        job_data = {
            "company_name": company_name,
            "title": job_title,
            "decription": decription,
            "link": link
        }

        job_db[keyword].append(job_data)



        
for page in range(pages):
    scraper_enginer("https://berlinstartupjobs.com", page + 1)

print(f"Pagination 후 엔지니어 일자리 스크래핑 한 데이터")
print("================================")
print(job_enginer_db)

for skill in skills:
    print(f"{skill}에 대한 일자리 스크래핑....")
    job_db[skill] = []
    scraper_job("https://berlinstartupjobs.com", skill)

for skill in skills:
    print(f"{skill}에 대한 일자리:")
    print(job_db[skill])
    print("================================")