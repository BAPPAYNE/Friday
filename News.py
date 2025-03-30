from bs4 import BeautifulSoup
import requests
def stockNews():
    URL = "https://pulse.zerodha.com/"
    page = requests.get(URL).text
    soup = BeautifulSoup(page, 'html.parser')
    data = soup.find('div',class_='desc')
    print(data.text)