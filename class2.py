# class2.py
# Developer 클래스를 정의하려고 하는데, id, name, skills 속성을 가지도록 하고 싶어요.
class Developer:
    def __init__(self, id, name, skills):
        self.id = id
        self.name = name
        self.skills = skills

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skills: {', '.join(self.skills)}")        

    #인스턴스를 생성
dev = Developer(1, "Alice", "Python")
dev.printInfo()
