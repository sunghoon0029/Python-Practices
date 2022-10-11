fr = open("./8888.txt", "r", encoding="UTF-8") # open(경로, 방식, 형식)
lines = fr.readlines() # 읽기
fr.close()

fw = open("./8888.txt", "w", encoding="UTF-8")
for line in lines: 
    update = input(f"전문장 : {line} \n 바꿀문장(취소는 c) : ")
    if update == 'c':
        fw.write(line.strip()) # strip() = 줄바꿈 제거
    else:
        fw.write(update)
    fw.write("\n")
fw.close()
