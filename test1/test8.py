# 제어문

# a = 5
# b = 5
# if a > b :
#     print(f"{a}는 {b}보다 크다")
#     print("2")
#     print("3")
# elif a < b :
#     print(f"{a}는 {b}보다 작다")
# else : # 위 조건이 다 아닐때에 실행
#     print("else")

# x = {"company" : "카카오", "isPartTime": True}
# # 1
# if x.get("company") == "카카오":
#     if x.get("isPartTime"):
#         print("대기업 비정규직원")
#     else:
#         print("대기업 정규직원")
# elif x.get("company") == "네이버":
#     print("대기업 직원이시네요")
# else:
#     print("중견기업 직원이시네요")
# # 2
# match x.get("company"):
#     case "카카오":
#         print("대기업 직원이시네요")
#     case "네이버":
#         print("대기업 직원이시네요")
#     case _:
#         print("중견기업 직원이시네요")

# Q. phone = {"name":"갤럭시", "version":"플립"}
# phone이 애플이면 와우
# 갤럭시면 version을 보고 
# 플립이면 접해네요 아니면 좋네요

phone = {"name":"갤럭시", "version":"플립"}
if phone.get("name") == ("애플"):
    print("와우")
elif phone.get("name") == ("갤럭시"):
    if phone.get("version") != ("플립"):
        ptint("좋네요")
    elif phone.get("version") == ("플립"):
        print("접히네요")
