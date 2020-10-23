import requests
from bs4 import BeautifulSoup
# urlopen : 네트워크에 존재하는 주소를 열어 주는 함수
from urllib.request import urlopen

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청 
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
res = requests.get('https://entertain.naver.com/movie')
myurl = 'https://entertain.naver.com/movie'
response = urlopen(myurl)

# print(res.content)
# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(response, 'html.parser')

# 3) 필요한 데이터 검색
title = soup.find_all('a', attrs={'class':'tit'})
# alen = len(soup.find_all('a'))

# 4) 필요한 데이터 추출
# print(len(title))
# print(alen)
for idx in range(len(title)):
    print(title[idx].get_text())