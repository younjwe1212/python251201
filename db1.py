#db1.py

import sqlite3

#연결객체 생성
con = sqlite3.connect(':memory:')
#커서객체 생성
cur = con.cursor()

#테이블 생성
cur.execute("CREATE TABLE phoneBook (name text, phoneNum text);")
#데이터 삽입
cur.execute("INSERT INTO phoneBook VALUES ('Alice', '123-4567');")

#입력파라미터처리
name ='김삿갓'
phoneNum ='987-6543'
cur.execute("INSERT INTO phoneBook VALUES (?, ?);", (name, phoneNum))   

#다중의 리스트를 입력
datalist = (("전우치","555-1234"), ("홍길동","555-5678"))
cur.executemany("INSERT INTO phoneBook VALUES (?, ?);", datalist)


#데이터 조회
cur.execute("SELECT * FROM phoneBook;")
for row in cur:
    print(row)  # ('Alice', '123-4567') 출력
