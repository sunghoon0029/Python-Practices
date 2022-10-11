print("Q3. ")

a = {"name" : "kim", "money" : 50000}
b = {"name" : "park", "money" : 30000}
print("%s는 %s보다 %s 있습니다." %(a["name"], b["name"], a["money"] - b["money"]))
print()
print("%s는 %s보다 %s 있습니다." %(a.get("name"), b.get("name"), a.get("money") - b.get("money")))
print("%s는 %s보다 %s 있습니다." %(b.get("name"), a.get("name"), b.get("money") - a.get("money")))
print()
print("%s는 %s 있습니다."%(a.get("name"), a.get("money")))
print("%s는 %s 있습니다."%(b.get("name"), b.get("money")))
print()
print("%s의 금액과 %s의 금액의 합은 %s 입니다."%(a.get("name"), b.get("name"), a.get("money") + b.get("money")))
print()
print("%s의 금액과 %s의 금액의 평균은 %d 입니다."%(a.get("name"), b.get("name"), (a.get("money") + b.get("money"))/2))