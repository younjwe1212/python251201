#날짜시간연습.py


#선택한 블럭을 주석철: ctrl + /
# import time
# print(time.time)
# time.sleep(10)
# print(time.time())
# print(time.gmtime())
# print(time.localtime())

import datetime

d1 = datetime.date.today()
print(d1)
d2 = datetime.datetime.now()
print(d2)
d3 = datetime.date(2025, 12, 25)
print(d3)

#날짜 간격 계산

d4 = datetime.timedelta(days=100)
print(d1 + d4)

#랜덤모듈

import random

print(random.random()) #0.0 ~ 1.0 미만의 임의의 실수
print(random.randint(1, 10)) #1~10 사이의 임의의 정수
print(random.choice(['가위','바위','보'])) #리스트에서 임의의 요소 선택
print(random.sample(range(1, 46), 6)) #1~45 사이의 숫자 중에서 6개를 임의로 뽑기



