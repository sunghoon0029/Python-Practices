# 반복문
a = ["a","b","c","d","e"]

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])

# for i in range(0,len(a)) : # 0 <= i < len(a) 반복
#     print(i)
#     print(a[i])

# for i in a :
#     print(i)

# re =0
# while re < 5 :
#     print(a[re])
#     re+=1 # re = re + 1

b = [1,2,3,4,5]
re = 0
while True :
    print(b[re])
    if(b[re]%2 == 0) :
        break # 반복 중지
    re+=1

for i in a :
    if i == "c" :
        break
    print(i)
