#BMI구하기 

h = int(input("키를 입력하세요. :"))/100
w = int(input("몸무게를 입력하세요. :"))

BMI = w / (h * h)

if BMI >= 25:
    print("비만입니다.")
elif BMI >= 23 and BMI < 25:
    print("과체중입니다.")
elif BMI >= 18.5 and BMI < 23:
    print("정상체중입니다.")
else:
    print("저체중입니다.")

#환전계산기

def exchage(m,c):
    if c in country_list:
        m_code = country_list.index(c)

    else:
        print("해당 국가 정보가 없습니다.")
        return

    result = round(m/rate[m_code],2)

    print(m, "원은", result, unit[m_code], "입니다.")


country_list = ['미국', '중국', '유럽'] #리스트를 만드고 
unit = ['달러', '위안', '유로', '엔'] 

money1 = int(input("환전(금액)원을 입력하세요:"))
country = input("국가를 입력하세요: ")


exchange(money1, country)

#Lab3 클릭하는 곳에 사각형을 만든다.

import turtle
t=turtle.Turtle()

def square(length): #화면에 그리는 square를 그리는 함수.
    for i in range(4):
        t.forward(length)
        t.left(90)


def drawit(x,y):#x,y 인자로 받는 함수 선언
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill


s = turtle.Screen()
s.onscreenclick(drawit)


#lab7

import turtle

def draw_maze(x,y):
    for i in range(2):
        t.penup()

        if i == 1:
            t.goto(x+100, y+100)


        else:
            t.goto(x,y)


        t.pendown()
        t.forward(300)
        t,right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)




def turn_left():
    t.left(1)
    t.forward(10)


def turn_right():
    t.right(10)
    t.forward(10)


t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

draw_maze(-300,300)


screen = turtle.Screen()
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")

t.penup()
t.goto(-300, 250)
t.pendown()


screen.listen()
screen.mainloop()


#한붓그리기 [핵심 아이디어]
#터틀 구성
#이벤트처리[마우스로 눌렀을 떄]

import turtle
t=turtle.Turtle()
t.shape("turtle")

t.pensize(10)

def draw(x,y):
    t.goto(x,y)
    
s = turtle.Screen()
s.onscreenclick(draw)

#이차함수 그래프 그리기

import turtle

t = turtle.Turtle()
t.shape("turtle")

def f(x):
    return x**2 + 1

t.goto(200,0)
t.goto(0,0)
t.goto(0,200)
t.goto(0,0)


for x in range(150):
    t.goto(x, 0.01*f(x))



