import requests
from bs4 import BeautifulSoup

url = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97'}

full_page = requests.get(url, headers=headers, timeout=10)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.find("div", id="PageContent_C119_Col00")
print(convert)

