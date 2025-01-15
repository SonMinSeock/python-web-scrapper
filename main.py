import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/remote-full-time-jobs"

reponse = requests.get(url)

soup = BeautifulSoup(reponse.content, "html.parser")
jobs = soup.find("section", class_="jobs").find_all("li")
print(jobs)
