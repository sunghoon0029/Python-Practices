# 2부터 20까지 짝수의 합

# 1.
# i = 0
# sum = 0

# for i in range(2, 21):
#     if i % 2 == 0:
#         i * 2
#     else:
#         i = 0
#     sum += i
# print(sum)

# 2.
# i = 2
# answer = 0
# while i <= 20:
#     if i%2 == 0:
#         answer += i
#     i += 1
# print(answer)

# 3.
answer = []
for i in range(2, 31):
    isPrimary = True # 소수인가?
    # i = 3, 2 <= j < 10
    for j in range(2, i):
        if i%j == 0:
            isPrimary = False
            break
    if isPrimary:
        answer.append(i)
print(answer)

# for el in range(1, 10):
#     for le in range(1, 10):
#         print(f"{el} * {le} = {le*el}")

# 별 찍기
# *
# **
# ***
# ****
# *****
text = "*"
for i in range(2, 7):
    st = ""
    for j in range(1, i):
        st = text*j
    print(text*j)