import requests
from bs4 import BeautifulSoup
import time
from pdf2image import convert_from_path
import wget
import os

URL = 'http://www.mrk-bsuir.by/ru'
recheck_time = 5 # seconds
DirLink = 'c:/Users/zen11/Desktop/Python/Mrk_bsuir_parser/'

def get_html(url):
    r = requests.get(url)
    print("page loaded")
    return r

def parse():
    html = get_html(URL)
    get_content(html.text)

    

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    pdf_link = soup.find("a", id="rasp").get('href')
    print(pdf_link)

    logs = open(DirLink + "logs.txt", 'r')
    old_link = logs.read()
    logs.close()

    while 1 == True:

        if pdf_link == old_link:
            print("Нового рассписания еще нет")
            time.sleep(recheck_time)
            parse()
        else:
            logs = open(DirLink + "logs.txt", 'w')
            logs.write(pdf_link)
            logs.close()

            wget.download(pdf_link, DirLink + 'file.pdf') # downloading PDF file

            pages = convert_from_path(DirLink + "file.pdf", 500) # Converting it to PNG
            x = 0 
            for page in pages:
                x = x + 1   # Adding +1 to every new file
                page.save(DirLink + "Images/page" + str(x) + '.jpg', 'JPEG') # saving it 

            os.remove(DirLink + "file.pdf")
            break



            

parse()
