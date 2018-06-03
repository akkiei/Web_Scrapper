from bs4 import BeautifulSoup
import requests
import requests.packages.urllib3

requests.packages.urllib3.disable_warnings()

fx=open('WEB.txt','r',encoding="utf-8") ## FILENAME me file ka name dalna
line=fx.readline()
l=open('email_mailto.txt','a',encoding='utf-8')

def web_imrove(url):
    print(url)

    try:
        source = requests.get(url)
    except Exception :
        l.write('\n')
        return 0

    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    emails = [a["href"] for a in soup.select('a[href^=mailto:]')]
    popo = str(emails)
    toto = popo.replace('mailto:', '')
    hoho = toto.replace('[', '')
    gogo = hoho.replace(']', '')
    mm = gogo.replace("'", "")
    if len(mm) is not 0:
        l.write(mm)
        l.write('\n')
        print(mm)
        return 1
    else:
        l.write('\n')
        return 0
        #print(mm)


while line:
    if line is '\n':
        l.write('\n')
        line=fx.readline()
        continue
    p = line.strip()

    if(  web_imrove('http://'+p) ):
        print('first')
    elif(  web_imrove('http://' + p+'/contact-us') ):
        print('second')
    else:
        web_imrove('http://' + p+'/contactus')

    line = fx.readline()