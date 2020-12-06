import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #가져온 html 문서를 lxml 파서를 통해서 soup이라는 객체를 만듬

#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})  #그 조건에 해당하는 모든 element를 찾음
# a element의 class 속성이 title인 모든 "a"라는 값 elemnet를 반환
for cartoon in cartoons:
    print(cartoon.get_text())
    