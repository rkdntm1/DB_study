import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

price = soup.find("table", attrs={"class": "tbl"}).find("tbody").find_all("tr")
for i, idx in enumerate(price):
    lst = idx.find_all("td")

    print("===============매물 {} ===============".format(i+1))
    print("거래 : ",lst[0].get_text().strip())
    print("면적 :  ",lst[1].get_text().strip()+"(공급/전용)")
    print("가격 :  ",lst[2].get_text().strip()+"(만원)")
    print("동 :  ",lst[3].get_text().strip())
    print("층 :  ",lst[4].get_text().strip())
