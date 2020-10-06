import requests
from bs4 import BeautifulSoup

URL = "https://www.vanguardngr.com/2020/10/ondo-decides-akeredolu-agboola-jegede-sign-peace-pact-promise-to-accept-election-verdict/"
response = requests.get(URL) 

soup = BeautifulSoup(response.content, 'html5lib')

heading = soup.find('h1', attrs = {'class':'entry-title'})
print(heading.text) 

time = soup.select_one('.posted-on.meta-tag')
print(time.text[3:])

news = soup.select('.entry-content > p')

for news_item in news[1:-1]:
    print(news_item.text)