#클래스1.py

#1)클래스 정의
class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "defalut name"
    def print(self):
        #print("mynameis{}".format(self.name))
        print(f"my name is {self.name}")
#2)인스턴스 새ㅐㅇ성

p1 = Person()

p1.print()
