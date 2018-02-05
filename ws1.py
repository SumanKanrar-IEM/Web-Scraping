from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), 'lxml')
print(bsObj.h1)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())


nameList = bsObj.findAll(text="the prince")
print(len(nameList))