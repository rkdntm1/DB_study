from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from newurl import News
import sys
from MyDB import DB
import time


#def search_news():
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
HEADERS = {"User-Agent": USER_AGENT}
main_url = 'https://news.naver.com/'

driver = wd.Chrome(executable_path='D:\chromedriver\chromedriver.exe')
driver.get(main_url)
#idwrap = driver.find_element_by_css_selector('#wrap')
#main = idwrap.find_elements_by_css_selector('#lnb ul li')
main = driver.find_elements_by_css_selector('#div.lnb>ul>li')
for idx in main:
    b = idx.find_element_by_css_selector('a')
    a = b.find_element_by_css_selector('.tx').text.strip()
    print(a)





    # idwrap = driver.find_element_by_css_selector('#wrap')
    #
    # menu_list = idwrap.find_elements_by_css_selector('#lnb ul li')
    # news_urls = []
    #
    # for index in menu_list:
    #     menu_li = index.find_element_by_css_selector('a')
    #     searchtxt = menu_li.find_element_by_css_selector('.tx').text.strip()
    #     # print(searchtxt)
    #     if searchtxt == 'IT/과학':
    #         menu_li.click()
    #         driver.implicitly_wait(2) #너무 많이 눌러서 크롤링 차단 못당하게 n초동안 웨이팅하고 클릭되게
    #         time.sleep(3)
    #         break;



# if __name__ == '__main__':
#     search_news()
#     sys.exit()