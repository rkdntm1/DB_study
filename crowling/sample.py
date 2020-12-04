from bs4 import BeautifulSoup
from urllib.request import urlopen
url = 'http://naver.com'
soup = BeautifulSoup(urlopen(url))


print(soup.prettify())