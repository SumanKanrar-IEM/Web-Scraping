import bs4 as bs
import urllib.request
import re
sauce = urllib.request.urlopen('https://www.fundoodata.com/citiesindustry/19/10/list-of-information-technology-(it)-companies-in-kolkata').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

links = soup.findAll('a', href=re.compile("\.html$"))
for link in links:
    if 'href' in link.attrs:
        print(link.attrs['href'])