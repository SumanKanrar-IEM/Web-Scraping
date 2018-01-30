import bs4 as bs
import urllib.request
sauce = urllib.request.urlopen('https://www.fundoodata.com/companies-detail/ITC-Ltd/31532.html').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

body = soup.body
#print(body)

for paragraph in body.find_all('p'):
    print(paragraph.text)


for div in soup.find_all('div', class_='body'):
    print(div.text)