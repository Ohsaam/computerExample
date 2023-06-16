##재귀함수 큰 수 팩토리알 -> 작은 수 팩토리알로 줄이면 된다.

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input("정수를 입력하세요:"))

f = fact(n)

print(n, "!은", f, "이다")

##프랙탈 나무 그리기

#터틀 그래픽 사용할 준비 
#나뭇가지의 규칙 찾기
#재귀함수 이용하여 나뭇가지 그리기

import turtle


def tree(length):
    if length > 5:
        t.forward(length) #거북이가 length만큼 선을 그린다.
        t.right(20)#20도 오른쪽으로회전한다.
        tree(length - 15) # length-15를 인수로 tree() 순환호출한다.
        t.left(40)#왼쪽으로 40도 회전한다. 
        tree(length - 15)
        t.right(20)
        t.backward(length)

t = turtle.Turtle()
t.color("green")#선의 색을 녹
색으로 한다.
t.speed(1)#속도를 제일 느리게한다.
t.left(90)
tree(90)
