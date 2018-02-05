import bs4 as bs
import urllib.request
import re

sauce = urllib.request.urlopen('https://www.fundoodata.com/companies-detail/ITC-Ltd/31532.html').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

#print(soup.title.text)

#print(soup.find_all('p'))

for paragraph in soup.find_all('script'):
    print(paragraph.text)
    pattern = re.compile("(\w+): '(.*?)'")
    fields = dict(re.findall(pattern, paragraph.text))
    #print(fields["address"])


#print(soup.get_text())

# for url in soup.find_all('a'):
#     print(url.get('href'))

##print(soup)



