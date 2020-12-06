#정규화
import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave ...
# caae, cabe, cace, cade ...

p = re.compile("ca.e")
# .(ca.e) : 하나의 문자를 의미 >care, cafe, case
# ^(^de) :문자열의 시작 >desk, destiny ...
# $(se$) : 문자열의 끝  > case, base

def print_match(m):
    #print(m.group()) #case 라는것이 정규식과 매칭이 되어 출력 / 매치되지않으면 에러 발생
    #아래처럼 간단히 표시
    if m:
        print("m.group()", m.group()) #일치하는 문자열 반환
        print("m.string:", m.string) # 입력받은 문자열
        print("m.start():", m.start()) #일치하는 문자열의 시작 index
        print("m.end()", m.end()) #일치하는 문자열의 끝
        print("m.span()", m.span()) #일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지않았습니다.")

# m = p.match("case") # 주어진 문자열의 처음부터 일치하는지 확인 /그래서 careless => 매칭됨
# print_match(m)

# m = p.search("good care") #search : 주어진 문자열중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") #findall : 일치하는 모든 것을 리스트형태로 반환
# print(lst)

# 1. p = re.complie("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열) : 주어진 문자열중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열) : 일치하는 모든 것을 리스트형태로 반환
# 원하는 형태 : 정규식
# .(ca.e) : 하나의 문자를 의미 >care, cafe, case
# ^(^de) :문자열의 시작 >desk, destiny ...
# $(se$) : 문자열의 끝  > case, base
