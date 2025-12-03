#web2.py
#웹크롤링을 위한 선언
from bs4 import BeautifulSoup
#웹서버에 요청

import urllib.request

#파일로 저장
f= open("clien.txt","wt", encoding="UTF-8")

for i in range(0,10):
#주소
    url = "https://www.clien.net/service/board/sold?&od=T31&category=0&po=" +str(i)
    print(url)

    #페이지 실행 결과를 문자열로 받기
    page = urllib.request.urlopen(url).read()
    #검색이 용이한 객체
    soup = BeautifulSoup(page, 'html.parser')

    lst = soup.find_all('span', attrs ={"data-role":"list-title-text"})
    for tag in lst:
        title = tag.text.strip()
        print(title)
        f.write(title+"\n")

f.close()




