import requests
from bs4 import BeautifulSoup

a = requests.get('https://s.search.naver.com/p/review/search.naver?rev=43&where=view&api_type=11&start=61&query=사과')

soup = BeautifulSoup(a.content.replace('\\', ''), 'html.parser')
print(soup)
