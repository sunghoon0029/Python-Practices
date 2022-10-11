# 정수 num이 짝수일 경우 "Even"을 반환하고 
# 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

# def solution(num):

#     if num % 2 == 0:
#         return f"Even"
#     else:
#         return f"Odd"

# print(solution(3)) # Odd
# print(solution(4)) # Even

# 형변환
def sum(a,b):
    print(type(a))
    print(type(b))
    try:
        if type(a) == int and type(b) == int:
            return a + b # return을 선언한 순간 끝
        else:
            return int(a) + int(b)
    except:
        return f"{a}랑 {b} 중 숫자가 아닌게 있습니다."
            
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))
while True:
    a = input("입력하세요")
    if a == "end":
        break
    b = input("입력하세요")
    if b =="end":
        break
    print(sum(a,b))


