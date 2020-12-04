# 모듈 가져오기
# pip install selenium
# pip install bs4
# pip install pymysql
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from newurl import News
import sys
from MyDB import DB
import time


def search_news():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
    HEADERS = {"User-Agent": USER_AGENT}
    main_url = 'https://news.naver.com/'

    driver = wd.Chrome(executable_path='D:\chromedriver\chromedriver.exe')
    driver.get(main_url)

    idwrap = driver.find_element_by_css_selector('#wrap')
    menu_list = idwrap.find_elements_by_css_selector('#lnb ul li')
    news_urls = []

    for index in menu_list:
        menu_li = index.find_element_by_css_selector('a')
        searchtxt = menu_li.find_element_by_css_selector('.tx').text.strip()
        # print(searchtxt)
        if searchtxt == 'IT/과학':
            menu_li.click()
            driver.implicitly_wait(2)
            break;

    submenu_lists = driver.find_elements_by_css_selector('#snb>ul.nav>li')
    print(len(submenu_lists))

    for sublist in submenu_lists:
        alist = sublist.find_element_by_css_selector('a')
        if alist.text.strip() == 'IT 일반':
            news_urls.append(alist.get_attribute('href'))
            alist.click()

            driver.implicitly_wait(3)
            break;

    title = driver.find_element_by_css_selector('div.list_header h3').text
    # print(title.text.strip())

    url = driver.find_elements_by_css_selector(".paging a")
    for i in url:
        if i.text != '다음':
            news_urls.append(i.get_attribute('href'))
        else:
            i.click()



    driver.implicitly_wait(2)
    print(title, news_urls)
    n = News(title, news_urls)

    driver.close()
    driver.quit()

    return n


if __name__ == '__main__':
    result = search_news()

    url = "127.0.0.1"
    user = "root"
    pwd = "kita"
    mydb = "t1"
    db = DB(url, user, pwd, mydb)

    print('db접속 : ', db)

    for index in result.url:
        db.inserdata(result.title, index)

    print('쓰기완료')
    sys.exit()
