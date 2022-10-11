fr = open("./8888.txt", 'r', encoding="UTF-8")
lines = fr.readlines()
fr.close()

fw = open("./8888.txt", 'w', encoding="UTF-8")
for line in lines:
    update_text = input(f"전 문장 : {line}\n 바꿀문장(취소는 c) :\t")
    if update_text == 'c':
        fw.write(line.strip())
    else:
        fw.write(update_text)
    fw.write("\n")
fw.close()