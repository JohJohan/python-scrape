import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.nl/Chocomel-0-Suiker-1L-Pak/dp/B0845FZ71F/ref=sr_1_1?__mk_nl_NL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=chocomel&pf_rd_i=18918385031&pf_rd_m=AC5DXSR5G8JPX&pf_rd_p=234c64b4-3b14-4acc-a263-4f37cfb6b6b3&pf_rd_r=DR5JDN3ZJQ6SQA924Q9F&pf_rd_s=merchandised-search-6&pf_rd_t=101&qid=1587825068&s=grocery&sr=1-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

def check_price():
    print('Starting request')
    page = requests.get(URL, headers=headers)

    print('Parsing request')
    soup = BeautifulSoup(page.content, 'html.parser')


    titel = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    print(titel.strip())
    print(price)
    converted_price = price[2:6]
    print(converted_price)

def run():
    check_price()

run()