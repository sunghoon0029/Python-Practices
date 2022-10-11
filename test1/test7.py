# list = [1,2,3,4,5,6,2,3,5,1]
# 위는 짝수 입니다.
# 위는 홀수 입니다.

# list1 = [1,2,3,4,5,6,2,3,5,1]
# # re = 0

# for el in list1 :
#     if el % 2 == 0:
#         print(f"{el} 은 짝수 입니다")
#     elif el % 2 == 1:
#         print(f"{el} 은 홀수 입니다")

# i = 0
# while i < len(list1) :
#     i+=1
#     if list1[i] % 2 == 0:
#         print(f"{list1[i]} 은 짝수 입니다")
#     elif list1[i] % 2 == 1:
#         # print(f"{list1[i]} 은 홀수 입니다")
#         continue # 반복문의 continue 뒤 실행 x
#         # break = 반복문이 끝남
#     print("---------{list1[i]}-----------")

# match case
# list1 = [1,2,3,4,5,6,2,3,5,1]
# for el in list1:
#     match el % 2:
#         case 1:
#             print(f"{el} 은 홀수 입니다")
#         case 2:
#             print(f"{el} 은 짝수 입니다")

# 람다 버전 3.6 부터
# 예제) list1 의 요소를 *2 해서 찍어봐라

# list3 = []
# for el in range(0, len(list1)):
#     list.append(list[el] * 2)
# list1 = [1,2,3,4,5,6,2,3,5,1]
# list2 = []
# for el in list1:
#     list2.append(el * 2)
# print(list2)
# # map 은 새로운 리스트를 만든다 (반환한다)
# list4 = list(map(lambda el: el ** 2, list1))
# print(list4)

# tmpd = {"name":"re","age":100}
# list5 = [tmpd,tmpd,tmpd]
# list6 = list(map(lambda el: el.copy(), list5))
# list7 = list5.copy()
# print(list5)
# print(list6)
# print(list7)
# list5.append(1)
# print()
# print(list5)
# print(list6)
# print(list7)
# tmpd["age"] = 10
# print()
# print(list5)
# print(list6)
# print(list7)
    
# list1 요소의 합 ? int (수)
# from functools import reduce


# list1 = [1,2,3,4,5,6,2,3,5,1]
# result = 0
# for el in list1:
#     result += el
# print(result)

# result2 = reduce(lambda x,y: x + y, list1)
# # 합계 구합때
# print(result2)

list1 = [1,2,3,4,5,6,2,3,5,1]
# 4이상 것 만(조건) 리스트를 만들려고 함
list0 = []
# 리스트를 만드려고 하니 리스트를 새로 선언함
for el in list1:
    print(el)
    if el >= 4:
        list0.append(el)
print(list0)

list01 = list(filter(lambda x: x >= 4, list1))
print(list01)
