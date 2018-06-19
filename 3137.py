#encoding=utf-8
import requests
from bs4 import BeautifulSoup
def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 20)
        r.encoding = r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        print 'requests error'
if __name__ == '__main__':
    url = 'https://www.qu.la/book/3136'
    html = getHtmlText(url)
    soup = BeautifulSoup(html,'html.parser')
    for i in soup.find_all('dd'):
        print i.text