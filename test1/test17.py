fr = open("./8888.txt", "r", encoding="UTF-8")
lines = fr.readlines()
fr.close()

fw = open("./8888.txt", "w", encoding="UTF-8")
for line in lines:
    update = input(f"전문장 : {line} \n 현재(취소는c) :")
    if update == 'c':
        fw.write(line.strip())
    else:
        fw.write(update)
    fw.write("\n")
fw.close()