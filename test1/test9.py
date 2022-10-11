# 반복문
# while for

# 0 <= i < 3
# for i in range(0,3):
#     print(i)

# list1 = ["a", "b", "c"]
# for i in range(0, len(list)):
#     print(list1[i])

# for element in list1:
#     print(element)

# index = 0
# while index < len(list1):
#     print(list[index])
#     index+=1

# break continue
# list1 = [9,4,2,1,6,7,5,4,3,7]
# 만약에 홀수면 2배 짝수면 일반적으로 리스트 만드는 중
# 만약 합이 20이 넘으면 끝

# list1 = [9,4,2,1,6,7,5,4,3,7]
# list2 = []
# i = 0
# sum1 = 0

# while i < len(list1):
#     sum1 += list1[i]
#     if list1[i] % 2 == 1:
#         list2.append(list1[i] * 2)
#     else:
#         list2.append(list1[i])
#     i+=1
#     if sum1 > 20:
#         break
# print(list2)

list1 = ["안", "녕", "하", "세", "요"] # while = 조건이 True인 동안 아래를 실행함
# index = 0
hi = ""
# while index < len(list1):
#     # print(list1[index])
#     hi += list1[index]
#     index+=1
# print(hi)

# for i in range(0, len(list1)): # 0 <= i < len(list1)
#     hi += list1[i]
# print(hi)

for element in list1:
    hi = hi + element
print(hi)

st = "안녕하세요"
for element in st:
    print(element)