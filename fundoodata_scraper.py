from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

html = urlopen("https://www.fundoodata.com/citiesindustry/19/10/list-of-information-technology-(it)-companies-in-kolkata")
bsObj = BeautifulSoup(html, 'lxml')




links = bsObj.findAll('a', href=re.compile("\.html$"))
final_links = set()
for link in links:
    links2 = link.get('href')
    final_links.add(links2)
    with open('links.csv', 'w') as myfile:
        filewriter = csv.writer(myfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for line in final_links:
            myfile.write(line)
            myfile.write('\n')


    #print(links2)




