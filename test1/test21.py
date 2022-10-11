# 자연수 뒤집어 배열로 만들기
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
# n은 10,000,000,000이하인 자연수입니다.

# ex)
# n	return
# 12345	[5,4,3,2,1]

# n = [1,2,3,4,5]
# print(n)
# n.reverse()
# print(n)

# def solution(n):
#     answer = []
#     return answer

# def solution(list):
#     list = []
#     for r in range(list(0), len(list-1)):
#         if r > 10000000000:
#             break
#         else:
#             list.append(r)

#     answer = list.reverse()
#     return answer

# list = [1,2,3,4,5]
# print(solution(list))

# def solution(n):
#     answer = []
#     for i in n:
#         answer.append(i)
#     return answer.reverse()
# print(solution(54665))

# list에서 제일 작은 수 제거하기
# 1개일땐 [-1]
# def solution(arr):
#     answer = []
#     # 1일때
#     if len(arr) == 1:
#         return [-1]
#     minNumber = 1000000
#     # 제일 작은 수
#     for a in arr:
#         if a  < minNumber:
#             minNumber = a
#     # 제거하기
#     for a in arr:
#         if minNumber != a:
#             answer.append(a)
#     return answer
# print(solution([10]))
# print(solution([4,3,2,1]))

# 1번 문제
# 배열 반대순서대로 정렬
# def solution(n):
#     answer = []
#     answer = list(str(n))
#     answer.reverse()
#     answer = list(map(int,answer))
#     return answer
# print(solution(1234))

# 2번 문제
# 가장 작은 수 제거하기
def solution(arr):
    answer = []
    # 1일때
    if len(arr) == 1:
        return [-1]
    minNumber = 1000000
    # 제일 작은 수
    for a in arr:
        if a  < minNumber:
            minNumber = a
    # 제거하기
    for a in arr:
        if minNumber != a:
            answer.append(a)
    return answer
print(solution([10]))
print(solution([4,3,2,1]))

# 3번 문제
# 두 정수 사이의 합
# def solution(a, b):
#     answer = 0
#     if b > a:
#         # list1 = list(range(a, b+1))
#         # answer = sum(list)
#         return sum(range(a,b+1))
#     elif a > b:
#         # list1 = list(range(b, a+1))
#         # answer = sum(list)
#         return sum(range(a,b+1))
#     else:
#         # answer = a
#         return answer
# print(solution(10, 5))

# 4번 문제
# 정수 제곱근 판별
def solu(n):
    answer = 0
    for i in range(1,n):
        if i * i == n:
            answer = (i+1)*(i+1)
            break
        elif i * i > n:
            break
    if answer == 0:
        return -1
    return answer
print(solu(121))
print(solu(3))