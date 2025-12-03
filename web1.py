#web1.py
#웹크롤링을 위한 선언
from bs4 import BeautifulSoup

# 파일을 로딩
page=open("Chap09_test.html","rt", encoding="UTF-8").read()

#검색이 용이한 객체 생성
soup =BeautifulSoup(page,'html.parser')

#전체를 출력
# print(soup.prettify())
#<p>를 몽땅검색
#print(soup.find_all('p'))

#print(soup.find('p'))

#print(soup.find_all('p', class_='outer-text'))

#태그 내부의 문자열만 추출:.text
for item in soup.find_all('p'):
    title = item.text.strip() #strip():앞뒤 공백제거
    title = title.replace("\n"," ") #줄바꿈문자 제거
    print(title)
    


