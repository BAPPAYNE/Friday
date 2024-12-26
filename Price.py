from bs4 import BeautifulSoup
import requests

def stockPrice(query="Binance coin price"):
    URL = "https://www.google.com/search?q=" + query
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')
    data = soup.find('div',class_='BNeawe iBp4i AP7Wnd')
    print(data.text)



stockPrice()

