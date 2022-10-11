# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

# phone_number는 길이 4 이상, 20이하인 문자열입니다.

# def solution(phone_number):
#     answer = ''
#     for i in range(0, len(phone_number)):
#         if i < len(phone_number)-4:
#             if phone_number[i] == "-":
#                 answer += "-"
#             else:
#                 answer += "*"
#         else:
#             answer += phone_number[i]
#     return answer
# phone_number = input("번호 000-0000-0000")
# print(solution(phone_number)) # "*******4444"
# # print(solution("027778888")) # "*****8888"

# # 뒤 4자리만 빼고 다 *
# # input 번호받아서 010-2222-2222
# # 뒷 4자리 만 살리고 ***-****-2222
# # 02-7777-7777 **-****-8888

# 파일 입출력
# 상대 경로 // 내 위치에서 -> 하고 싶은 곳
# . 현재위치 c/test
# .. c
# . 현재위치 c/test/test1
# ../test12.py
# 절대 경로
# C:/test/test2/test.py

# f = open("./test.txt", 'w') # 텍스트 작성
# f.write("hi")
# f.write("\n")
# f.write("bye")
# f.close()

# f = open("./test.txt", 'a') # 텍스트 수정 및 추가
# f.write("           sdf")
# f.close()

# def open(filename, type):
        # filename 이 있는가
    # if type == 'w'
        # 글쓰기모드
    # elif type == 'r'
        # 읽기모드

from asyncore import write


f = open("./8888.txt", 'r', encoding="UTF-8") # 텍스트 읽기
lines = f.readlines()
# lines = ["hi", "bye"]
for line in lines :
    print(line)

# fw = open("./test.123", 'w')
# for line in lines :
#     if line == "ga":
#         fw.write("na")
#     else:
#         fw.write(line)
# fw.close()

# fe = open("./8888.txt", 'w', encoding="UTF-8")
# for line in lines :
#     line = line.strip()
#     if line == "나":
#         fe.write("나나\n")
#     elif line == "가":
#         fe.write("가가\n")
#     else:
#         fe.write(f"{line}")
#     fe.write("\n")

# fe.close()