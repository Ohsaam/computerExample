result = 0

def calculate_area():
    global result #전역변수  사용 할 때 키워드 
    result = 3.14 * r ** 2

r = float(input("원의 반지름 : "))
calculate_area()
print(result)

#디폴트 인수[msg]

def greet(name, msg):
    print("안녕",name)

greet("철수", "좋은 아침!")

#결과 : 안녕 철수 좋은아침!

#매개변수가 없을 때, 
def greet(name,msg = '잘지내죠?'):
    print("안녕", name, ',' + msg)

greet("영희")

#결과 : 안녕 영희, 잘 지내죠? 

def calc(x,y,z):
    return x+y+z

print(calc(10,20,30))



