
import  requests
from MyDB import DB
from bs4 import BeautifulSoup
import time
from collections import  defaultdict
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}

def get_html(news_url):
  #request로 자료 받기
  #print(news_url)
  data=''
  try:
      response=requests.get(news_url,headers=HEADERS)
      data=response.text
      #print('test', data)
      time.sleep(2)
  except Exception as e:
      print('에러')
  finally:
       response.close()
  return data

def get_db_data():
  host="127.0.0.1"
  user="root"
  pwd="kita"
  mydb="t1"
  db=DB(host, user,  pwd, mydb)
  #print("db연결 완료",db)

  newsurl_list=db.listdata()  #database에서 자료 가져오기
  return newsurl_list

def collect_sub_urls(url): #sublist
    data_list=[]
    soup=BeautifulSoup(url, 'lxml')
    lisdata=soup.find('ul', class_="type06_headline").find_all('dl')

    for index in lisdata:
       #print(index)
       time.sleep(1)
       newsdic = defaultdict(dict)

       dts=index.find_all('dt')

       if len(dts)==2 :
           _img=dts[0].find('a').find('img')
           imgsrc=_img["src"].strip()
           a=dts[1].find('a')
           alink=a['href']
           title=a.text.strip()
           newsdic['title']=title
           newsdic["img"]= imgsrc
           newsdic['alink']=alink
       else:
          a=dts[0].find('a')
          alink=a['href']
          title=a.text.strip()
          newsdic['title']=title
          newsdic['alink']=alink
       data_list.append(newsdic)

    return data_list

def collect_sub_content(sub):
     time.sleep(1)
     suburl= sub.get('alink')
     title=sub.get('title')
     try:
        response = requests.get(suburl,headers=HEADERS)
        html=response.text
        soup=BeautifulSoup(html,'lxml')
        _div=soup.find('div', class_='_article_body_contents').text.strip()
        print('title', title)
        print('url', suburl)
        print('content', _div)
     except Exception as e:
         print(e)
     finally:
         response.close()
    # _div_content=_div.text.strip()
    # print(_div_content)

if __name__ == '__main__':
    newsurl_list=get_db_data()


    html=get_html(newsurl_list[0]['url'])
    suburl=collect_sub_urls(html)
    collect_sub_content(suburl[0])

    #      time.sleep(1)


#과제
#편입종목 https://finance.naver.com/sise/entryJongmok.nhn?&page=1
#종목별- 현재가 받아보기