import requests
import string
from bs4 import BeautifulSoup
import os

a=set()  # AFTER making 1000 websites link , change file handler to read('r') from write mode('w') ...
#b=set()

head_= open("Heading_TRIP_LV.txt", "w", encoding="utf-8")
address_= open("Address_TRIP_LV.txt", "w", encoding="utf-8")
phone_=open("Phone_TRIP_LV.txt", "w", encoding="utf-8")
site_= open("Website_TRIP_LV.txt", "w", encoding="utf-8")
email_=open("email_TRIP.txt","w",encoding="utf-8")
#################################################################

def trade_spider(max_pages) :
    page=1
    print('\nNow Crawling Entire page to acquire all the links ...')
    while page <=max_pages :
        print('/-Page Number='+str(page) )
        url=str( page_number(page) )
        #print(url)
        #po='https://www.yelp.com'
        po='https://www.tripadvisor.in'
        source=requests.get(url)
        plain_text=source.text
        soup=BeautifulSoup(plain_text,'html.parser')
        for link in soup.find_all('a',class_='property_title'):
           #print('..')
           href=link.get('href')
           #print(po+href)
           a.add(po+href)

        page +=1
    print(" Page Crawling Completed!!\nNow going to each and every URL and Acquiring all the data\n   ")

##########################################################

def address(url):
    source=requests.get(url)
    plain_text=source.text
    soup=BeautifulSoup(plain_text,'html.parser')
    add = soup.find(class_= 'street-address' )
    dre = soup.find(class_='extended-address')
    ss = soup.find(class_='locality')
    if add is None:
        #print('ooh.....')
        address_.write('\n')
        return
    #address_ = open("Address_TRIP_LV.txt", "a", encoding="utf-8")
    if dre is not None:
        q = str(dre.get_text(strip=True))
    else:
        q=''
    if ss is not None:
        r = str(ss.get_text(strip=True))
    else:
        r=''
    p=str(add.get_text(strip=True))
    #print(p+q+r)
    address_.write(p)
    address_.write(',')
    address_.write(q)
    address_.write(r)
    address_.write('\n')
    phone_no(soup)
    # print(p+q+r)


####################################################

def heading(url,o):
    #error='See you later!'
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    heading = soup.find('h1',class_='heading_title ')
    if heading is None:
        head_.write('\n')
        return 0
        # popo=heading.text.strip()
        # if str(popo) is str(error):
        #  head_.write('\n')
        #  return 0
    #head_ = open("Heading_TRIP_LV.txt", "a", encoding="utf-8")
    popo = heading.get_text(strip=True)
    #print(popo)
    head_.write(str(popo))
    head_.write('\n')
    #head_.close()
    #print(popo)
    return 1
#########################################################

def page_number(page):
    m = str((page - 1) * 30)
    url='https://www.tripadvisor.in/RestaurantSearch-g45963-oa'+m+'-p8-Las_Vegas_Nevada.html#EATERY_LIST_CONTENTS'
    #url='https://www.tripadvisor.in/RestaurantSearch-g45963-oa'+m+'-Las_Vegas_Nevada.html#EATERY_LIST_CONTENTS'
    #print(url)
    return url

############################################################

def phone_no(soup):
    #source = requests.get(url)
    ##plain_text = source.text
    #soup = BeautifulSoup(plain_text, 'html.parser')
    phone=soup.find(class_='blEntry phone')
    if phone is None:
        phone_.write('\n')
        email(soup)
        return 0
    #phone_ = open("Phone_TRIP_LV.txt", "a", encoding="utf-8")
    tele=phone.get_text(strip=True)
    phone_.write( str( tele) )
    phone_.write('\n')
    email(soup)
    #print(tele)

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
    site_ = open("Website_TRIP_LV.txt", "a", encoding="utf-8")
    #web=soup.find( 'a' , { 'target' : '_blank' ,'rel' : 'noopener nofollow' } )
    #if web is None:
     #   print('  ULLU ')
      #  return 0
    #site=web.get_text(strip=True)
    site='www.'+website
    site_.write( str(site) )
    site_.write('\n')
    #print(site)

################################################
def email(soup):
    #mail = soup.select('a[href^=mailto]')
    #for i in mail:
    #    if i.string != None:
     #     print( (i.string.encode('utf-8').strip()) )
   # email_ = open("email_TRIP.txt", "a", encoding="utf-8")
    emails = [a["href"] for a in soup.select('a[href^=mailto:]')]
    popo=str(emails)
    toto=popo.replace('mailto:','')
    hoho=toto.replace('[','')
    gogo=hoho.replace(']','')
    mm=gogo.replace("'","")
    #print(mm)
    if len(mm) is not 0:
        email_.write(mm)
        email_.write('\n')
        # print(mm)
    else:
        email_.write('\n')
        #print('\n')
    web_imrove(soup)
    #email_.close()
    #print(popo.replace('mailto',''))
    #for mail in soup.find_all('a',href='mailto:'):
    #print(mail)
    #em=mail.get('href')
    #print(em)

###########################################################

def web_imrove(soup):
    url=soup.find('a',text='Improve This Listing')
    if url is None:
         site_('\n')
         return
    #site_ = open("Website_TRIP_LV.txt", "a", encoding="utf-8")
    p='https://www.tripadvisor.in'+url.get('href')
    p = 'https://www.tripadvisor.in' + url.get('href')
    src = requests.get(p)
    p_text = src.text
    sop = BeautifulSoup(p_text, 'html.parser')
    popo=sop.find(id='website')
    qq=popo.get('value')
    site_.write(qq)
    site_.write('\n')
    #site_.close()
    #print(qq)


########################################################## GLOBAL SPACE

trade_spider(6) ## NO OF PAGES ...

set_file=open('Set_TRIP_All_links.txt','w',encoding='utf-8') # ISKO
for val in a:  ### this will write all links from set to set_file.txt to maintain records ...
    set_file.write( str(val) )          # COMMENT
    set_file.write( '\n' )           # KAR
set_file.close()                    # DENA

fx=open('Set_TRIP_All_links.txt','r')
line=fx.readline()
o=int(1)
while line:
    if (o > int(250) ):
        print(' \n *****BREAKING OUT OF THE CODE**** \n') # HAR BAR 250 urlS delte krdena SET_YELP_ALL_LINKS.txt se/.....
        break
    p=line.strip()
    #print(p)
    print(o,end='')
    FH=heading(p,o)
    #print(p)
    if FH is 1:
      print(' ~~')   ## this means -> the number on the left side is done.
      address(p)
      #phone_no(p)
      #email(p)
      #web_imrove(p)
    line = fx.readline()
    o+=1

head_.close()
site_.close()
address_.close()
phone_.close()
email_.close()