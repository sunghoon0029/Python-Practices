from msilib.schema import Class


# 파이썬은 무슨 언어인가?
# 절차지향

# -type
#     int, str, list, set, tuple, dict
# 동작 타이핑
# 장점 : 자동으로 타입 지정
# 단점 : 오류 발생 취약
# (int) a = 1
# (str) a = "str"
# (list) a = []
# (set) a = {}
# (tuple) a = ()
# (dict) a = {key : value}

# -제어문
#     if, elif, else
#     case

# -반복문
#     for in :
#     while
    #     break, continue
    # lambda(map, reduse, filter)
    # list = [9,1,2,4,3]
    # def sum(x, y) :
    #     print(f"{x} {y}") # formet
    #     return x + y
    # a = reduse(lambda (x, y): x+y, list1)

    # user = {"id:id", "pass:pass", "name:""}
    # names = ["kim", "lee", "perk"]
    # namelist = list(map(lambda x : {"id:id", "pass:pass", "name:x"}, names))
    # print(namelist)

    # findUser = list(filter(lambda x : x.get("name") == "park", namelist))
    # print(findUser)

# -함수
#     def :

# def sum(a,b) :
#     return a+b
# sum(1,2) # 1,2 = 인수

# def sum(*a) : # a = tuple
# sum(1,2,3,4)
# def sum(**a) : # a = dict
# sum(name=kim, age = 50)

# name = "kim" # 전역 변수
# def printName(name):
#     name = "lee" # 지역 변수

# -파일 입출력
# f = open(파일, mode, )
# encording UTF-8

# ex) C:\test -> C:\test\test2
# -상대결로
#     ./test2
# -절대경로
#     C:\test\test2

# 입력받고 싶을 떄 : input

# -Class(객체지향) = 중복되는 코드를 묶어서 처리하기 위해
# class name(상속):
#     def __init__(self) -> None:
#         super().__init__()
# 부모클래스에 접근 할때 : super()
# def __init__(self): # self = 자신

# import = 다른 경로에 있는 파일을 불어올 때
# import re
# import random 등등



# -정규식 개념
# search, match
# ex) whtjdgns0029@naver.com < 검색해서 일치 하는지 판단


# ----------------------------------------------------

# 스크립트 언어 = 소스 코드를 한 줄씩 읽어서 곹바로 실행
#     ex) python 문법으로 코드를 작성 했는데
#         컴퓨터 언어는 0110
#         컴파일 : python -> 컴퓨터 언어
#         파일을 컴퓨터 언어로 바꾸어 따로 파일을 실행
#         스크립트언어는 바로 실행

# 플랫폼 독립적 : os 관계없이 실행가능 (os = 운영체계)
