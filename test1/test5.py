# 제어문
a = 10
b = 5
# print(f"a > b (a > b) = True 크다 False 작다")
# : 뒤에는 tab 혹은 띄어쓰기

str1 = ""
if a>b :  # 조건이 True 면 아래 문장을 실행한다
    str1 = "크다"
    print(f"a > b 크다")
elif a<b : # elif : 위의 조건이 아니면(False) 실행
    str1 = "작다"
    print(f"a > b 작다")
else : # else : if 도 elif 둘아 False 일때 실행
    str1 = "같다"
    print(f"a = b [str1]")

c = [1,2,3,4,5]
if len(c) > 3 :
    print(c[0])
if len(c) > 2 : 
    print(c[0])  