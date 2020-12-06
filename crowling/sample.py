import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page=1"
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

for data in data_rows:
    print(data)

