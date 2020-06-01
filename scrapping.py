from bs4 import BeautifulSoup
import requests

source = requests.get('https://timesofindia.indiatimes.com/blogs/politics/').text
soup = BeautifulSoup(source, 'html5lib')
for head in soup.find_all('div', class_='media-body'):
    tiit = head.h2.a.text
    print(tiit)
    print()

for body in soup.find_all('div', class_='content'):
    piit = body.p.text
    print(piit)
    print()