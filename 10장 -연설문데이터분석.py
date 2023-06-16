infile = open("input.txt", "r")
outfile = open("output.txt", "w")


word_dic = {}
total_count = 0


for line in infile:
    line = line.rstrip()
    word_list = line.split()


    for word in word_list:
        word = word.lower() #소문자로 변경
        word = word.strip(',')#콤마삭제
        word = word.strip('.')



        if word in word_dic:
            word_dic[word] += 1
            total_count += 1


        else:
            word_dic[word] = 1
            total_count += 1

#단어별 빈도수를 결과파일에 저장하고 총 단어수를 화면에 출력 
result = ""
for key in sorted(word_dic.keys()):
    result = key + " " + str(word_dic[key]) + '\n'
    outfile.write(result)


print("총 단어 수 = ", total_count)

#입력 파일 출력 파일 닫기

outfile.close()
infile.close()
