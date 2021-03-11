import requests
from bs4 import BeautifulSoup

url = "https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/"
page=requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
i=1
#open file w=write, r=read, a=append
file = open('testfile.txt','w')
for div in soup.findAll('div',{'class':'tv-screener-table__symbol-container'}):
    #add each line
    file.writelines(div.find('a')['href']+"\n")
    if i==5:break
    i=i+1
#close file
file.close()

