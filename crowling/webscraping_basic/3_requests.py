import requests

res = requests.get("http://google.com") #url에 접속해서 정보를 가져옴
#print("응답코드:", res.status_code) #200이면 정상
res.raise_for_status() #올바른 html을 가져왔으면 ok , 아니면 에러 발생
#아래 내용을 한줄로 줄이기 가능
# if res.status_code == requests.codes.ok: # = 200
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", 'w', encoding="utf8") as f: #가져온 내용을 파일로 만들어보기
    f.write(res.text)
