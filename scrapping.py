from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.instagram.com/explore/tags/plage/")
data = r.text

soup = BeautifulSoup(data, 'lxml')

if soup:
    for link in soup.find_all('img'):
        print(link.get('src'))