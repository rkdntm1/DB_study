import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="

title = []
price = []
page_lst= []
pages = 10
for page in range(1,pages):
    res = requests.get(url+str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_1"}).find_all("tr")

    for row in data_rows:
        lsts = row.find_all("td")
        if len(lsts) <= 1:  # 의미없는 데이터 스킵용
            continue
        data = [lst.get_text().strip() for lst in lsts] # 빈칸을 없애고 텍스트 가져옴
        title.append(data[0])
        price.append(data[1])
        page_lst.append(page)
last = [item for item in zip(page_lst, title, price)]
for i in last:
    print(i)

