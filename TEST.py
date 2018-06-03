import selenium from web
import requests
import string
from bs4 import BeautifulSoup
import linecache
import multiprocessing
import time

head_= open("Heading_zagat_LV.txt", "a", encoding="utf-8") # files which contains data
address_= open("Address_zagat_LV.txt", "a", encoding="utf-8")



def heading(soup):
    time.sleep(10)
    #print(soup)
    heading = soup.find('h1')
    print(heading)
    if heading is None:
        print('nhi')
        head_.write('\n')
        return 0
    popo = heading.get_text(strip=True)
    print(popo)
    head_.write(str(popo))
    head_.write('\n')
    return 1

def address(soup):
    add = soup.find(class_= 'zgt-business-detail-text flex' )
    if add is None:
        address_.write('\n')
        return
    p=str(add.get_text(strip=True))
    print(p)
    address_.write(p)
    address_.write('\n')




o=1                                 #     IMPORTANT :/ uncomment to collect links ...
fx=open('Set_zagat_All_links.txt','r')
line=fx.readline()
p = line.strip()
print(p)
print(o, end='')
source = requests.get(p)
plain_text = source.text
soup = BeautifulSoup(plain_text, 'html.parser')
FH = heading(soup)
address(soup)