# main = 내가 실행시킬 것
# java는 무조건 main start

from Calculator.add import add
from Calculator.calc import Calc
from Calculator.diff import diff
from Calculator.person import Person
from User.age import showAge
from User.name import showName
from test2.testInput import testInput


def main():
    # count = 0
    # count = add(count,4)
    # count = diff(count,10)
    # print(count)
    # text = testInput()
    # print(text)

    # a = Person()
    # a = Person()
    # a = Person()
    # print(a.__dict__)
    # print(a)
    # print(a.count)

    Calc.add(1,3)

    # showName("park")
    # showAge(21)

# main()
# class animal():
#     def __init__(self) -> None:
#         print('동물')
#         pass