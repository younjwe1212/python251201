# Person.py 
"""
이 파일은 아주 쉬운 말로 '사람 상자'를 만들어요.
- Person: 기본 사람 상자(아이디, 이름)
- Manager: 관리자 상자(직함 포함)
- Employee: 직원 상자(기술 포함)

각 상자에는 정보를 화면에 보여주는 printInfo() 함수가 있어요.
맨 아래에는 예제로 여러 사람을 만들고 정보를 보여주는 코드가 있어요.
(5살 어린이도 이해하도록 아주 쉽게 설명해 두었어요.)
"""

class Person:
    """
    Person 클래스는 한 사람을 나타내요.
    
    아주 쉽게:
    - 사람을 만들 때 아이디(id)와 이름(name)을 줘요.
    - printInfo()를 부르면 그 사람이 누군지 글자로 보여줘요.
    """

    def __init__(self, id, name):
        """
        새 사람을 만들 때 실행되는 함수예요.
        
        간단히:
        - id: 숫자나 글자(사람을 구별하는 이름표)
        - name: 그 사람의 이름(예: '영희')
        이 두 가지를 상자에 넣어 저장해요.
        """
        self.id = id
        self.name = name
    
    def printInfo(self):
        """
        이 함수는 그 사람의 정보를 화면에 보여줘요.
        
        출력 예:
        ID: 1, Name: 김철수
        아주 쉬운 문장으로 읽을 수 있게 해줘요.
        """
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    """
    Manager는 Person에서 조금 더 특별한 사람이에요.
    
    추가로:
    - title(직함)이 있어요. 예: '부장', '팀장'
    printInfo()를 부르면 기본 사람 정보와 직함을 같이 보여줘요.
    """

    def __init__(self, id, name, title):
        """
        매니저를 만들 때는 id, name, title을 넣어요.
        title은 그 사람이 어떤 일을 맡고 있는지 알려주는 말이에요.
        """
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        """
        매니저의 정보를 보여줘요.
        먼저 Person의 정보(ID와 이름)를 보여주고,
        그 다음에 직함을 한 줄 더 보여줘요.
        """
        super().printInfo()
        print(f"Title: {self.title}")


class Employee(Person):
    """
    Employee는 일반 직원이에요.
    
    추가로:
    - skill(기술)이 있어요. 예: 'Python', 'Java'
    printInfo()를 부르면 기본 사람 정보와 기술을 같이 보여줘요.
    """

    def __init__(self, id, name, skill):
        """
        직원을 만들 때는 id, name, skill을 넣어요.
        skill은 그 사람이 잘하는 일을 써요.
        """
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        """
        직원의 정보를 보여줘요.
        먼저 Person의 정보(ID와 이름)를 보여주고,
        그 다음에 기술을 한 줄 더 보여줘요.
        """
        super().printInfo()
        print(f"Skill: {self.skill}")


# 테스트 코드
if __name__ == "__main__":
    """
    아래 예제는 여러 사람(매니저와 직원)을 만들어서
    printInfo()로 하나씩 화면에 보여주는 부분이에요.
    
    그냥 파일을 실행하면 이 부분이 실행돼요.
    """
    instances = [
        Manager(1, "김철수", "부장"),
        Employee(2, "이영희", "Python"),
        Manager(3, "박민준", "과장"),
        Employee(4, "최순신", "Java"),
        Manager(5, "정재호", "팀장"),
        Employee(6, "한동욱", "JavaScript"),
        Manager(7, "오영준", "이사"),
        Employee(8, "강보람", "C++"),
        Manager(9, "류지연", "감독"),
        Employee(10, "송준호", "SQL")
    ]
    
    for instance in instances:
        instance.printInfo()
        print("-" * 40)
p1 = Person(100,"전우치")
