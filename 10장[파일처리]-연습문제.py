# "r" 읽기모드 /// "w" 쓰기 모드 /// "a" 추가 모드 /// "r+" 읽기와 쓰기 모드

import csv

f = open('d:\\input.csv','r')
data = csv.reader(f)

for line in data:
    print(line)


f.close()


#split메서드

a = "All`s well that ends well"
a.split()


#답은 [Alls, 'well', 'that', 'ends', 'well']


#파일에 데이터 쓰기
outfile = open("d:\\phones1.txt", "w")
outfile.write("전우치 010-1234-5678\n")
outfile.write("홍길동  010-1234-5678\n")
outfile.close()

# 파일에서 한 줄 씩 읽어보기

infile = open("d:\\phones.txt", "r")

line = infile.readline().rstrip()
while line != "":
    print(line)
    line = infile.readline().rstrip()

infile.close()

#파일에서 한 줄 씩 읽어오기 version2


infile = open("d:\\phones.txt", "r")

line1 = infile.readline()
print(line1) #홍길동 010-1234-5678

line2 = infile.readline()
print(line2)#김철수 010-1234-5678

infile.close()

#파일의 모든 줄을 읽는 함수는 read()다.

infile = open("d:\\phones.txt", "r")
lines = infile.read()
print(lines)
infile.close()
#홍길동 010-1234-1234
#김철수 010-4567-8205

#파일의 모든 줄을 읽는 함수는 파일 객체의 readlines()도 있다.
infile = open("d:\\phones.txt", "r")
lines = infile.readlines()
print(lines)
infile.close()
