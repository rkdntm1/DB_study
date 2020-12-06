import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

for i in range(1, 6):
    # print("페이지 : ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)


    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup: BeautifulSoup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"txt":"광고"})
        if ad_badge:
            #print("    <광고 상품 제외합니다>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()

        #애플 제품 제외
        if "Apple" in name:
            #print(" <Apple 상품 제외")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격
        rate = item.find("em", attrs={"class":"rating"})#평점
        if rate: # 평점이 없는 항목이 있어서 오류가 뜸으로 이렇게 처리
            rate = rate.get_text()
        else:
            #print(" <평점 없는 상품 제외합니다.")
            continue

        rate_cnt = item.find("span", attrs={"class":"rating_total_count"})#평점 수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text() #예 :(26)
            #rate_cnt = rate_cnt[1:-1]
           # print("리뷰 수 ", rate_cnt)
        #else:
           # print(" <평점 수 없는 상품은 제외합니다")
        #평점 4.5 이상 리뷰 50개 이상


        link = item.find("a", attrs= {"class":"search-product-link"})["href"]

        if float(rate) >= 4.5:
            # print(name, price, rate, rate_cnt)
            print(f'제품명 : {name}')
            print(f'가격 : {price}')
            print(f'평점 : {rate}점 ({rate_cnt}개)')
            print("비로가기 : {}".format("https://www.coupang.com"+link))
            print("-"*100) # 줄긋기


