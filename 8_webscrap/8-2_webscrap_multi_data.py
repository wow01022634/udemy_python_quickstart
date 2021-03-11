import requests
from bs4 import BeautifulSoup

url = "https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/"
page=requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
i=1
for div in soup.findAll('div',{'class':'tv-screener-table__symbol-container'}):
    price=soup.find("a",class_="current-price")
    print(div.find('a')['href'])
    if i==5:
        break
    i=i+1


