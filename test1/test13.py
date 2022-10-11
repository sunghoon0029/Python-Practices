# 3,6,9 게임
# 들어온 숫자에 3,6,9
# c
# 계속 지속되어야하는 게임
# 369369 현재 {i}
# 입력 다음 할 것

# def sum(a):
#     if int(a) % 3 == 0:
#         if a == "c":
#             return int(a) + 1
#         else:
#             return f"졌습니다"
#     else:
#         return int(a) + 1

# while True:
#     a = input("369369 현재 : ")
#     if a == "항복":
#         print("졌습니다")
#         break
#     print(sum(a))

# def game():
#     i = 0
#     while True:
#         i += 1
#         print(f"현재 값 {i}")
#         myInput = input(f"현재 값 {i} ")
#         answer = str(i + 1)
#         for c in str(i+1):
#             if c=="3" or c=="6" or c=="9":
#                 answer = "c"
#         if myInput == answer:
#             print("맞았다")
#         else:
#             print("game over")
#             break
   
def game(cur, myInput):
 
        answer = str(cur + 1)
        for c in str(cur + 1):
            if c=="3" or c=="6" or c=="9":
                answer = "c"
        if myInput == answer:
            print("맞았다")
            return True
        else:
            print("game over")
            return False

i = 0
while True:
    i += 1
    myInput = input(f"현재 값 {i} ")
    isWin = game(i,myInput)
    if(not isWin):
        break
