import requests
from bs4 import BeautifulSoup


url = "http://www.preciosas-promessas.com.br/109.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup)