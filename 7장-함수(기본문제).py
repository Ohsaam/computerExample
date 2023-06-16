def print_adress(name):

    print("서울특별시 종로구 1번지")
    print("파이썬 빌딩 7층")
    print(name)
    


print_adress("홍길동")
print_adress("오지환")
print_adress("김갑샘")


###파라미터 예제 

def get_sum(start, end):
    sum = 0
    for i in range(start, end-1):
        sum+=i
    print("sum = ", sum)

get_sum(1,10)
get_sum(1,20)


## 결과 sum = 54, sum = 210



def calculate_area(radius):
    area = 3.14*radius **2 #원주률 구하는 공식 적용
    return area

c.area = calculate_area(5.0)
print(c.area)

area.sum = calculate_area(5.0) * calculate_area(10.0)

print(area_sum)


#결과 값 78.5 // 392.5


#여러개의 인자를 반환할 수 있다. 
def get_input():
    return 2,3

x,y = get_input()
print(x, ",", y)

# 2,3 도출


##교수가 좋아하는 문제 (짝홀수 판단하기)

def judge(num):
    if num % 2 == 0:
        print("짝수")
        return

    print('홀수')

#사용자 입력부분 
num = int(input("자연수를 입력하세요"))
judge(num)



##터틀[반복문 버전]
import turtle
t = turtle.Turtle()
t.shape("turtle")


for i in range(4):
    t.forward(100)
    t.left(90)


t.up()
t.goto(-200, 0)
t,down()

for i in range(4):
    t.forward(100)
    t.left(90)

#터틀[함수버전]

import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(100)
        t.left(90)
        
square(100)
t,up()
t.goto(-300,0)
t.down()
square(100)

