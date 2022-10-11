# 계산기 만들기

# def add(a,b):
#     return a+b

# def diff(a,b):
#     return a-b

# i = 0
# i = add(i, 10)
# i = diff(i, 5)
# print(i)

# j = 0
# j = add(j, 10)
# j = diff(j, 5)
# print(j)

# class
# class Calculator:
#     def __init__(self) -> None:
#         self.result = 0

#     def add(self,b):
#         self.result += b

#     def diff(self,b):
#         self.result -= b



from Animal import Animal
from Arm import Arm
from Cat import Cat
from Dog import Dog
from Human import Human
from Leg import Leg
# from test2.test19 import Calculator

# 클래스 = 하나의 물체를 만들기위해 사용
# 상속 = 공통 코드를 줄이기위해 사용

# cal1 = Calculator()
# cal1.add(10)
# cal1.diff(5)
# print("cal1\t{cal1.result}")

# cal2 = Calculator()
# cal2.add(10)
# cal2.diff(5)
# print("cal2\t{cal2.result}")

# cal3 = Calculator()
# cal3.add(10)
# cal3.diff(5)
# print("cal1\t{cal3.result}")

# user1 = User("bit", "1234")
# user1.printUser()
# user1.change_id("pppp")
# user1.printUser()

# l = Leg("left", "park")
# print(l.side)
# print(l.name)
# l.setName("kim")
# print(l.name)

# an = Animal()
# print(an.name)
# an.__setattr__("name", "?")
# print(an.__dict__)

# 부모 클래스를 상속받아 사용가능
# cat = Cat()
# cat.printSound()
# print(cat.name)

dog = Dog()
dog.printSound()
print(dog.name)
print(dog.master)
print(dog.__dict__)