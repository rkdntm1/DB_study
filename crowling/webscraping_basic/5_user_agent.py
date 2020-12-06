# 웹사이트에서는 접속하는 사용자의 정보를 알 수 있음 (header 정보)
import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = "http://nadocoding.tistory.com"
res = requests.get(url, headers =headers)
#res.raise_for_status()
with open("nadocoding.html", 'w', encoding="utf8") as f: #가져온 내용을 파일로 만들어보기
    f.write(res.text)
