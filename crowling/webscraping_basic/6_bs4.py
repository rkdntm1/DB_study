import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #가져온 html 문서를 lxml 파서를 통해서 soup이라는 객체를 만듬
# print(soup.title.get_text())
# print(soup.a) #soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element의 속성정보 출력
#print(soup.a["href"]) # a element의 속성값 정보를 출력

#print(soup.find("a", attrs ={"class":"Nbtn_upload"} ))
#"a"에 해당하는 첫번째 열 가져옴 #class =Nbtn_upload인 a element를 찾아줘

#print(soup.find(attrs ={"class":"Nbtn_upload"} ))
# class =Nbtn_upload인 어떤 element를 찾아줘

#print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text())
# print(rank1.next_sibling) # 찾은 엘리먼트 정보로부터 다음 엘리먼트로 넘어감
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling # 이전으로
# print(rank2.a.get_text())
# print(rank1.parent)

# rank2 = rank1.find_next_sibling("li") #li 기준으로 다음 엘리먼트를 찾음
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# webtoon = soup.find("a", text ="맘마미안-71화" )
# print(webtoon)