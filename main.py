from bs4 import BeautifulSoup
import requests

source= requests.get('https://traveltriangle.com/blog/travel-story/').text
soup = BeautifulSoup(source, 'html5lib')
for article in soup.find_all('article'):
    kk = article.h3.a.text
    print(kk)

    jj = article.find('div', class_='blog-excerpt').p.text
    print(jj)


    print()
