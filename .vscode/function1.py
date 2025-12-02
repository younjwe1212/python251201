#fuction1.py

#1)함수를 정의

def setValue(newValue):
    x = newValue
    print("함수내부:",x)

#2)호출

result = setValue(5)
print(result)

#함수를 정의
def swap(x,y):
    return y,x

#  ghcnf
result = swap(3,4)
print(result)

print("--- 기본값을 명시")
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

print("--키워드인지--")
def connectURI(server, port):
    strURL="https://"+ server +""

def union(*ar):
    #지역변수
    result= []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","EGG"))
print(union("HAM","egg", "spam"))
