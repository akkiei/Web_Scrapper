#### ZAGAT

import requests
import string
from bs4 import BeautifulSoup
import linecache
import multiprocessing
################################################################################################


head_= open("Heading_zagat_LV.txt", "a", encoding="utf-8") # files which contains data
address_= open("Address_zagat_LV.txt", "a", encoding="utf-8")
phone_=open("Phone_zagat_LV.txt", "a", encoding="utf-8")
site_= open("Website_zagat_LV.txt", "a", encoding="utf-8")
email_=open("email_zagat.txt","a",encoding="utf-8")
#################################################################

def trade_spider(max_pages) :
    page=1
    print('\nNow Crawling Entire page to acquire all the links ...')
    while page <=max_pages :
        print('/-Page Number='+str(page) )
        url=str( page_number(page) )
        base_link='https://www.tripadvisor.in'
        source=requests.get(url)
        plain_text=source.text
        soup=BeautifulSoup(plain_text,'html.parser')
        for link in soup.find_all('a',class_='property_title'):
           href=link.get('href')
           a.add(base_link+href)

        page +=1
    print(" Page Crawling Completed!!\nNow going to each and every URL and Acquiring all the data\n   ")

##########################################################

def address(soup):
    add = soup.find(class_= 'street-address' )
    dre = soup.find(class_='extended-address')
    ss = soup.find(class_='locality')
    if add is None:
        address_.write('\n')
        return
    if dre is not None:
        q = str(dre.get_text(strip=True))
    else:
        q=''
    if ss is not None:
        r = str(ss.get_text(strip=True))
    else:
        r=''
    p=str(add.get_text(strip=True))
    address_.write(p)
    address_.write(',')
    address_.write(q)
    address_.write(r)
    address_.write('\n')


####################################################

def heading(soup):
    heading = soup.find('h1',class_='heading_title ')
    if heading is None:
        head_.write('\n')
        return 0
    popo = heading.get_text(strip=True)
    head_.write(str(popo))
    head_.write('\n')
    return 1

#########################################################

def page_number(page):
    m = str((page - 1) * 30)
    url='https://www.tripadvisor.in/Restaurants-g32810-Oakland_California.html#EATERY_LIST_CONTENTS'
    return url

############################################################

def phone_no(soup):
    phone=soup.find(class_='blEntry phone')
    if phone is None:
        phone_.write('\n')
        return 0
    tele=phone.get_text(strip=True)
    phone_.write( str( tele) )
    phone_.write('\n')
#    email(soup)

###############################################################

def website(soup):
    web = soup.find('a',rel='noopener')
    if web is None:
        site_.write('\n')
        return
    website = web.get_text( strip=True )
    site='www.'+website
    site_.write( str(site) )
    site_.write('\n')

################################################

def email(soup):

    emails = [a["href"] for a in soup.select('a[href^=mailto:]')]
    popo=str(emails)
    toto=popo.replace('mailto:','')
    hoho=toto.replace('[','')
    gogo=hoho.replace(']','')
    mm=gogo.replace("'","")
    if len(mm) is not 0:
        email_.write(mm)
        email_.write('\n')

    else:
        email_.write('\n')

###########################################################

def web_imrove(soup):

    url=soup.find('a',text='Improve This Listing')
    if url is None:
         site_('\n')
         return
    p='https://www.tripadvisor.in'+url.get('href')
    p = 'https://www.tripadvisor.in' + url.get('href')
    src = requests.get(p)
    p_text = src.text
    sop = BeautifulSoup(p_text, 'html.parser')
    popo=sop.find(id='website')
    qq=popo.get('value')
    site_.write(qq)
    site_.write('\n')

##########################################################
##########################################################  GLOBAL SPACE
##########################################################
                                       #     IMPORTANT :/ uncomment to collect links ...
fx=open('Set_TRIP_All_links.txt','r')
line=fx.readline()
o=int(1)
while line:
    if (o > int(166) ):
        print(' \n *****BREAKING OUT OF THE CODE**** \n') # HAR BAR 250 urlS delte krdena SET_YELP_ALL_LINKS.txt se/.....
        break
    p=line.strip()
    print(o,end='')
    source = requests.get(p)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    FH=heading(soup)
    if FH is 1:
      address(soup)
      phone_no(soup)
      email(soup)
      web_imrove(soup)
      print(' DONE')  ## this means -> the number on the left side is done.
    line = fx.readline()
    o+=1

head_.close()
site_.close()
address_.close()
phone_.close()
email_.close()