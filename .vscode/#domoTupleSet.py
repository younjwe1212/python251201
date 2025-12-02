#domoTupleSet.py

#set형식 연습
a = {1,2,3,3}
b = {3,4,4,5}

print(a)
print(b)
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple연습
tp = (10,20,30)
print(len(tp))
print(tp.index(20))
print(tp.count(10))

#함수를 정의
def calc(a,b):
    return a+b, a*b

#호출
result = calc(3,4)
print(result[0], result[1])

#한방에 입력
print("id:%s, name:%s" % ("kim","김유신"))

