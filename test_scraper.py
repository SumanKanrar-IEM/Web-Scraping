from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("https://www.fundoodata.com/citiesindustry/19/10/list-of-information-technology-(it)-companies-in-kolkata"+pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll("a", href=re.compile("\.html$")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
            #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")