import requests
from bs4 import BeautifulSoup

url = "https://www.fool.com/quote/nasdaq/apple/aapl/"
page=requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
price=soup.find("span",class_="current-price")
print(price.text)