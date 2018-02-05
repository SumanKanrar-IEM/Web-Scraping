# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, 'lxml')
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])




# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import datetime
# import random
# import re
#
# random.seed(datetime.datetime.now())
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html, 'lxml')
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
#     href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links = getLinks("/wiki/Kevin_Bacon")
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)



from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
            #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")