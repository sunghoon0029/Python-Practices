# 문제 1.
a = 80
b = a%2 == 0
print("%s은 짝수가 %s이다" %(a, b))
print()
print(f"80은 짝수인가 {80%2==0}")

# 문제 2.
list1 = [2,1,5,6,2,40,50,2,5,32]
list2 = [4,6,2,3,9,10,2,3,42,5,4,63]
union = list(set(list1) & set(list2))
union.sort()
print(union)
print(union[len(union)-1])
print()


