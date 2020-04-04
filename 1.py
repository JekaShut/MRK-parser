import requests
from bs4 import BeautifulSoup
#import dryscrape
from selenium import webdriver

url = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97'}

driver = webdriver.Chrome()
driver.get(url)
#sess = dryscrape.Session()
#sess.visit(url)
#response = sess.body()

full_page = driver.page_source  #requests.get(url, headers=headers)

soup = BeautifulSoup(full_page, features="lxml") #BeautifulSoup(full_page.content, 'html.parser')

convert = soup.find("div", id="confirmedCases").text
print(convert)

driver.quit()