# EXPERIMENTAL!!!!! WORK IN PROGRESS....
# YELP
import linecache
import multiprocessing
import requests
from bs4 import BeautifulSoup


a=set()  # AFTER making 1000 websites link , change file handler to read('r') from write mode('w') ...

head_ = open("Heading_Yelp_LV.txt", "a", encoding="utf-8")
address_ = open("Address_yelp_LV.txt", "a", encoding="utf-8")
phone_=open("Phone_Yelp_LV.txt", "a", encoding="utf-8")
site_ = open("Website_Yelp_LV.txt", "a", encoding="utf-8")

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
           href=link.get('href')
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
    return 1

####################################################

def heading(url):
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    heading = soup.find('h1')
    if heading is None:
        return 0
    popo = heading.get_text(strip=True)
    head_.write(str(popo))
    head_.write('\n')
    return 1
#########################################################

def page_number(page):
    m = str((page - 1) * 30)
    url='https://www.yelp.com/search?find_desc=Restaurants&find_loc=Oakland,+CA&start='+m
    return url

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
    site='www.'+website
    site_.write( str(site) )
    site_.write('\n')
    #print(site)






###########################################################
########################################################## GLOBAL SPACE

#trade_spider(33) ## NO OF PAGES ...

#set_file=open('Set_Yelp_All_links.txt','w') # ISKO
#for val in a:  ### this will write all links from set to set_file.txt to maintain records ...
   # set_file.write( str(val) )          # COMMENT
 ##   set_file.write( '\n' )           # KAR
#set_file.close()                    # DENA


#fx=open('Set_Yelp_All_links.txt','r')
#line=fx.readline()
#o=1
#while line:
 #   if (o>5):        # HAR BAR 250 urlS delte krdena SET_YELP_ALL_LINKS.txt se/.....
  #      break
  #  p=line.strip()

  #  print(o,end='')
  #  FH=heading(p,o)
  #  if FH is 1:                     ## this means -> the number on the left side is done.
  #    address(p)
  #    phone_no(p)
  #    website(p)
  #    print(' DONE')
  #  line = fx.readline()
  #  o+=1



def trade_(i):
    print('Jarvis',i)
    line =linecache.getline('Set_Yelp_All_links.txt',i)
    #print(line)
    call_jarvis(line,i)

def call_jarvis(line,i):
    p = line.strip()
    #print(o, end='')
    #print('\n')
    FH = heading(p)
    if FH is 1:  ## this means -> the number on the left side is done.
        address(p)
        phone_no(p)
        website(p)
        print(i,' DONE')


if __name__ =='__main__':
   for i in range(1,10,5):  # YHA PE NO. OF PAGES DAL DO [10] ki jagah
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

