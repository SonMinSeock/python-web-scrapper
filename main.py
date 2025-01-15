import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/remote-full-time-jobs"

reponse = requests.get(url)

soup = BeautifulSoup(reponse.content, "html.parser")
jobs = soup.find("section", class_="jobs").find_all("li")[:-1]

for job in jobs:
    title = job.find("span", class_="title").text

    company, position, region = job.find_all("span", class_="company")
    region = region.text
    company = company.text
    position = position.text

    print(title, region, company, position, "-----\n")