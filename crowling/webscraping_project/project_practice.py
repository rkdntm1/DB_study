import requests
from bs4 import BeautifulSoup
import re

def createres(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text , 'lxml')
    return soup
def print_n(idx, title, link):
    print("{}. {}".format(idx + 1, title))
    print(" (링크 : {}".format(link))
#[오늘의 날씨]
def scrape_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%8B%9C"
    soup = createres(url)
    print("[오늘의 날씨]")
    # 날씨 요약 부분
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 기온(현재, 최저, 최고)
    curtp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    mintp = soup.find("span", attrs={"class":"min"}).get_text().strip()
    maxtp = soup.find("span", attrs={"class": "max"}).get_text().strip()
    # 강수확률
    morning = soup.find("span", attrs={"class":"point_time morning"}).get_text()
    afternoon = soup.find("span", attrs={"class": "point_time afternoon"}).get_text()
    # 미세 먼지, 초미세 먼지
    dust = soup.find("dl", attrs={"class":"indicator"})
    dust1 = dust.find_all("dd")[0].get_text().strip()
    dust2 = dust.find_all("dd")[1].get_text().strip()


    #출력
    print(cast)
    print("현재 {}, (최저 {} / 최고 {})".format(curtp, mintp, maxtp))
    print("오전 {} / 오후 {}".format(morning, afternoon))
    print()
    print("미세먼지 {}".format(dust1))
    print("초미세먼지 {}".format(dust2))
    print()

def scrape_news():
    url = "https://news.naver.com"
    soup = createres(url)
    print(" [오늘의 뉴스] ")
    news = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit =3)
    for idx, new in enumerate(news):
        title = new.find("a").get_text().strip()
        link = url + new.find("a")["href"]
        print_n(idx, title, link)
    print()

def scrape_news_IT():
    print(" [ IT/과학 뉴스 ] ")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = createres(url)
    news = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit =3)

    for idx, new in enumerate(news):
        id = 0
        photo =new.find("dt",attrs={"class":"photo"})
        if photo:
            id = 1

        title = new.find_all("a")[id].get_text().strip()
        link = new.find_all("a")[id]["href"]
        print_n(idx, title, link)
    print()

def scrape_eng():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = createres(url)
    engs= soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})

    print(" [영어 지문]")
    for eng in engs[len(engs)//2:]: # 절반 이상 부분 값 가져오기
        print(eng.get_text().strip())
    print(" [한글 지문]")
    for eng in engs[:len(engs)//2]: # 절반 미만 부분 가져오기
        print(eng.get_text().strip())

def scrape_coro():
    url ="https://corona-live.com/"
    soup = createres(url)
    cov = soup.find("div", attrs={"class":"Layout__SBox-c6bc3z-0 dEQorJ"}).get_text()
    print("실시간확진자수: ", cov)








if __name__ == "__main__":
    scrape_weather()
    scrape_news()
    scrape_news_IT()
    scrape_eng()
    scrape_coro()