#### TRIP ADVISOR

import linecache
import multiprocessing
import requests
import string
from bs4 import BeautifulSoup

################################################################################################

#a=set() #it contains all the links to crawl...

head_= open("Heading_TRIP_LV.txt", "a", encoding="utf-8") # files which contains data
address_= open("Address_TRIP_LV.txt", "a", encoding="utf-8")
phone_=open("Phone_TRIP_LV.txt", "a", encoding="utf-8")
site_= open("Website_TRIP_LV.txt", "a", encoding="utf-8")
email_=open("email_TRIP.txt","a",encoding="utf-8")
#################################################################

##########################################################

def address(soup):
    add = soup.find(class_= 'zgt-business-detail-text flex' )
    if add is None:
        address_.write('\n')
        return
    p=str(add.get_text(strip=True))
    address_.write(p)
    address_.write('\n')


####################################################

def heading(soup):
    print('HEADING')
    head = soup.find('h1',class_='heading_title ')
    if head is None:
        head_.write('\n')
        return 0
    popo = head.get_text(strip=True)
    head_.write(str(popo))
    head_.write('\n')
    return 1

#########################################################

def page_number(page):
    m = str((page - 1) * 30)
    url='https://www.tripadvisor.in/RestaurantSearch-g45963-oa'+m+'-p8-Las_Vegas_Nevada.html#EATERY_LIST_CONTENTS'
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
  #  email(soup)

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


def trade_(i):
    print('Jarvis',i)
    line =linecache.getline('Set_TRIP_All_links.txt',i)
    #print(line)
    call_jarvis(line,i)

def call_jarvis(line,i):
    p = line.strip()
    #print(o, end='')
    #print('\n')
    source = requests.get(p)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    FH = heading(soup)
    if FH is 1:    ## this means -> the number on the left side is done.
        address(soup)
        phone_no(soup)
        email(soup)
        web_imrove(soup)
        print(i,' DONE')


if __name__ =='__main__':
   for i in range(1,20,5):  # YHA PE NO. OF PAGES DAL DO [10] ki jagah
        p = multiprocessing.Process(target=trade_, args=( i , )   )
        q = multiprocessing.Process(target=trade_, args=(i+1,)  )
        r = multiprocessing.Process(target=trade_, args=(i + 2,) )
        s = multiprocessing.Process(target=trade_, args=(i + 3,) )
        t = multiprocessing.Process(target=trade_, args=(i + 4,) )

        p.start()
        q.start()
        r.start()
        s.start()
        t.start()
