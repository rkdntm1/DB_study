import requests
import re
from bs4 import BeautifulSoup
from newurl import News
import sys
from MyDB import DB

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = "https://finance.naver.com/sise/entryJongmok.nhn?&page="

def search_news():
    title = []
    price = []
    page_lst = []
    pages = 11
    for page in range(1, pages):
        res = requests.get(url+str(page), headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        #data_rows = soup.find("table", attrs={"class":"type_1"}).find_all("tr")
        data_rows = soup.find("table", class_="type_1").find_all("td",class_="ctg") # 종목명 가져올떄
        L = [i.find_next_sibling("td") for i in data_rows] # 현재가 가져올때

        return data_rows, L
        # for row in data_rows:
        #     lsts = row.find_all("td")
        #     if len(lsts) <= 1:  # 의미없는 데이터 스킵용
        #         continue
        #
            # data = [lst.get_text().strip() for lst in lsts] # 빈칸을 없애고 텍스트 가져옴
            # title.append(data[0])
            # price.append(data[1])
            # page_lst.append(page)


    # last = [item for item in zip(page_lst, title, price)]
    # return last




if __name__ == '__main__':
    t, p = search_news()
    for i, j in zip(t, p):
        print(i.text.strip(), j.text.strip())
    # url = "127.0.0.1"
    # user = "root"
    # pwd = "kita"
    # mydb = "t1"
    # db = DB(url, user, pwd, mydb)
    #
    # print('db접속 : ', db)
    #
    # for index in result:
    #     db.inserdata(index[0], index[1], index[2])
    #
    # print('쓰기완료')
    # sys.exit()