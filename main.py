from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

time.sleep(5)

page.click("button.Aside_searchButton__rajGo")
# page.locator("button.Aside_searchButton__rajGo").click()

time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(5)

page.keyboard.down("Enter")

time.sleep(5)

page.click("a#search_tab_position")

time.sleep(5)

for x in range(5):
    page.keyboard.down("End")
    time.sleep(5)


content = page.content()

playwright.stop()

soup = BeautifulSoup(content, "html.parser")
