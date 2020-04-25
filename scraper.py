import requests
from bs4 import BeatifulSoup

URL = ''

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeatifulSoup(page.conten, 'html.parser')

print(soup.prettify())
