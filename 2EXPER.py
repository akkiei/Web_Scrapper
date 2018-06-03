# YELP EXPERIMENT >>>>>>><<<<<<<

import requests
from bs4 import BeautifulSoup
import os

a=set()

head_ = open("Heading_Yelp_LV.txt", "w", encoding="utf-8")
address_ = open("Address_yelp_LV.txt", "w", encoding="utf-8")
phone_=open("Phone_Yelp_LV.txt", "w", encoding="utf-8")
site_ = open("Website_Yelp_LV.txt", "w", encoding="utf-8")

#################################################################

def trade_spider(max_pages) :
    page=1
    print('\nNow Crawling Entire page to acquire all the links ...')
    while page <=max_pages :
        print('/-Page Number='+str(page) )
        url=str( page_number(page) )
        #print(url)
        po='https://www.yelp.com'
        #po='https://www.tripadvisor.in/'
        source=requests.get(url)
        plain_text=source.text
        soup=BeautifulSoup(plain_text,'html.parser')
        for link in soup.find_all('a',class_='biz-name js-analytics-click'):
           #print('..')
           href=link.get('href')
           ##print(po+href)
           a.add(po+href)

        page +=1
    print(" Done !! Now going to each and every URL and Acquiring all the data\n   ")

##########################################################

def address(url):
    source=requests.get(url)
    plain_text=source.text
    soup=BeautifulSoup(plain_text,'html.parser')
    add = soup.find('address')
    if add is None:
        address_.write('\n')
        return
    addrr=add.get_text(strip=True)
    address_.write( str( addrr ) )
    address_.write('\n')
        #print(add.text.strip())
    return 1

####################################################

def heading(url,o):
    error='See you later!'
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
   # for heading in soup.find_all('h1',class_='biz-page-title embossed-text-white shortenough',limit=1):
    heading=soup.find('h1')
    if heading is None:
        return 0
         #popo=heading.text.strip()
         #if str(popo) is str(error):
         #  head_.write('\n')
         #  return 0
    popo=heading.get_text(strip=True)
    head_.write(str(popo))
    head_.write('\n')
         #print(o,popo)
    return 1

#########################################################

def page_number(page):
    url='https://www.yelp.com/search?find_desc=Best+Restaurants&find_loc=Las+Vegas,+NV&start='
    m=str( (page -1)*10 )
    if page is 1:
        return (url)
    else:
        temp='https://www.yelp.com/search?find_desc=Best+Restaurants&find_loc=Las+Vegas,+NV&start='+m
       ## temp='https://www.tripadvisor.in//Restaurants-g667805-oa'+m+'-Kanpur_Kushi_Nagar_District_Uttar_Pradesh.html#EATERY_LIST_CONTENTS'
        return temp

############################################################

def phone_no(url):
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    phone=soup.find(class_='biz-phone')
    if phone is None:
        phone_.write('\n')
        return 0
    tele=phone.get_text(strip=True)
    phone_.write( str( tele) )
    phone_.write('\n')
    #print(tele)
    return 1

###############################################################

def website(url):
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    web = soup.find('a',rel='noopener')
    if web is None:
        site_.write('\n')
        return
    website = web.get_text( strip=True )

    #web=soup.find( 'a' , { 'target' : '_blank' ,'rel' : 'noopener nofollow' } )
    #if web is None:
     #   print('  ULLU ')
      #  return 0
    #site=web.get_text(strip=True)
    site='www.'+website
    site_.write( str(site) )
    site_.write('\n')
    #print(site)






###########################################################
########################################################## GLOBAL SPACE

trade_spider(1) ## No

set_file=open('Set_Yelp_All_links.txt','w')
for val in a:  ### this will write all links from set to set_file.txt to maintain records ...
    set_file.write( str(val) )
    set_file.write( '\n' )
set_file.close()

o=1
while a:
    print(o,end='')
    p=a.pop()
    FH=heading(p,o)
    #print(p)
    if FH is 1:
      print(' ~~')
      FA=address(p)
      #if FA is 1:
      phone_no(p)
      website(p)

    o+=1

head_.close()
site_.close()
address_.close()
phone_.close()
