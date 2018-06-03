#import threading
import multiprocessing
import requests
import string
import linecache
from bs4 import BeautifulSoup
################################################################################################
set_file = open('Set_TRIP_All_links.txt', 'r')


def trade_spider(url) :
   # page=1
    #print('\nNow Crawling Entire page to acquire all the links ...')
    #while page <=max_pages :
        #print('/-Page Number='+str(page) )
        #url=str( page_number(page) )
        base_link='https://www.yelp.com'
       # try:
        print(url)
        source=requests.get(url)
       # except Exception:
        #    set_file.write('\n')
         #   return
        plain_text=source.text
        soup=BeautifulSoup(plain_text,'html.parser')
        for link in soup.find_all('h1',class_='biz-page-title embossed-text-white shortenough'):
           href=link.text
           print(href)
           #set_file.write(base_link+href)
           #set_file.write('\n')

       # print(" Page Crawling Completed!!\nNow going to each and every URL and Acquiring all the data\n   ")



def page_number(page):
    m = str((page - 1) * 20)
    url='https://www.yelp.com/search?find_loc=Providence,+RI,+USA&start='+m+'&cflt=restaurants'
    return url


def trade_(i):
    print(linecache.getline('Set_TRIP_All_links.txt',i))
#    print(line)
    #trade_spider(line)






if __name__ =='__main__': # YHA PE NO. OF PAGES DAL DO ## ki jagah
   for i in range(0,10,5):
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
      #  p.join()
       # q.join()
       # r.join()
        #s.join()
