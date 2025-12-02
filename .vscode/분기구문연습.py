#분기구문연습.py
 
score =int(input("점수를 입력:"))

if 90 <= score <=100:
    grade = "A"
elif 80 <= score < 90:
    grade ="B"
elif 70 <=score <80:
    grade ="C"
else:
    grade = "D"

print("등급은", grade)

value = 5
while value > 0:
    print(value)
    value -=1
print("===for in루프===")
lst = [10,20,30]
for item in lst:
    print(item)

print("---range()---")
print(list(range(10)))
print(list(range(1,11)))
print(list(range(2000,2026)))
print(list(range(1,32)))

print("---리스트 내장---")
lst = list(range(1, 11))
print(lst)
print([i**2 for i in lst if i >5])
tp = ("apple", "kiwi")
print([len(i) for i in tp])

    