import requests
from bs4 import BeautifulSoup
import os

a=set()
b=set()

#################################################################

def trade_spider(max_pages) :
    page=1
    while page <=max_pages :
        print('Now Crawling Entire page to acquire all the links ...\n Page Number='+str(page) )
        url=str( page_number(page) )
        print(url)
        #po='https://www.yelp.com/'
        po='https://www.tripadvisor.in/'
        source=requests.get(url)
        plain_text=source.text
        soup=BeautifulSoup(plain_text,'html.parser')
        for link in soup.find_all('a',target='_blank',class_='property_title'):
           print('..')
           href=link.get('href')
           a.add(po+href)

        page +=1
    print(" Done !! Now going to each and every one  ")

##########################################################

def each_link(url):
    source=requests.get(url)
    plain_text=source.text
    soup=BeautifulSoup(plain_text,'html.parser')
    for add in soup.find_all(class_='address ui_column is-12'):
        print(add.text)

####################################################

def heading(url,o):
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for heading in soup.find_all(class_='heading_title '):
        print(o,heading.text.strip())

##########################################################

def page_number(page):
    ##url='https://www.yelp.com/search?find_desc=Best+Restaurants&find_loc=Las+Vegas,+NV&start='
    url = ' https://www.tripadvisor.in/Restaurants-g667805-Kanpur_Kushi_Nagar_District_Uttar_Pradesh.html'
    #po = 'https://www.tripadvisor.in/'
    #source = requests.get(url)
    #plain_text = source.text
    #soup = BeautifulSoup(plain_text, 'html.parser')
    m=str( (page-1)*30)
    ##m=str( (page -1)*10 )
    if page is 1:
        return (url)
    else:
       ## temp='https://www.yelp.com/search?find_desc=Best+Restaurants&find_loc=Las+Vegas,+NV&start='+m
        temp='https://www.tripadvisor.in//Restaurants-g667805-oa'+m+'-Kanpur_Kushi_Nagar_District_Uttar_Pradesh.html#EATERY_LIST_CONTENTS'
        return temp
    #for link in soup.find_all('a', {'data-page-number':page} ):
     #   href=link.get('href')
      #  print(po+href)
       # if(href) is None:
        #    return 1
       # return (po+href)

############################################################



trade_spider(1)
o=1
while a:
    p=a.pop()
    heading(p,o)
    print(p)
    each_link(p)
    o+=1