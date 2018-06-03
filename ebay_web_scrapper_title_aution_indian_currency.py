import requests
from bs4 import BeautifulSoup
import os

def trade_spider(max_pages):
    page=1
    p=1
    fx = open("MyTextyy.txt", "w", encoding="utf-8")
    while page <=max_pages:
        url='http://www.ebay.in/sch/Indian-Coins/45136/i.html?_pgn='+str(page)+'&_skc=50&rt=nc'
        print(page)
        source=requests.get(url)
        plain_text=source.text
        soup=BeautifulSoup(plain_text,'html.parser')
        for link in soup('a',{'class':'vip'}):
            href=link.get('href') # for links
            title= link.string # for title plain text without any html tags
            print(title)
            #price=''
            #for rs in soup('b', {'class': 'bold'}):
            #price = rs.string


            if title is None:
              continue
            #title=title.encode("utf-8")
            #print(title.encode("utf-8"))
           # fx.write(str(p))
            ##fx.write('-')
            #fx.write(title)
            #fx.write('   |  ')
            ##fx.write(price)
            #fx.write('\n')
            p +=1

        page +=1

trade_spider(1)