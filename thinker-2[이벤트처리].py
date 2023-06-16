#이벤트처리

from tkinter import *

def process():
    print("안녕하세요?")

window = Tk()

button = Button(window, text = "클릭하세요", command = process)
button.pack()

window.mainloop()

#버튼 이벤트처리 
from tkinter import *


def process():
    e2.insert(0, "100")

window = Tk()

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")

l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column =1)
e2.grid(row=1, column =1)

b1 = Button(window, text = "화씨->섭씨", command=process)
b2 = Button(window, text = "섭씨->화씨")
b1.grid(row=2, column =0)
b2.grid(row=2, column =1)


window.mainloop()


#버튼 이벤트처리-2
from tkinter import *


def process():
    temperature = float(e1.get())
    mytemp = (temperature-32) * 5/9
    e2.insert(0,str(mytemp))

window = Tk()

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")

l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column =1)
e2.grid(row=1, column =1)

b1 = Button(window, text = "화씨->섭씨", command=process)
b2 = Button(window, text = "섭씨->화씨")
b1.grid(row=2, column =0)
b2.grid(row=2, column =1)


#위젯 색상과 폰트 변경
from tkinter import *

def process():
    temperature = float(e1.get())
    mytemp = (temperature-32) * 5/9
    e2.insert(0,str(mytemp))

window = Tk()

l1 = Label(window, text="화씨", font = 'helevetica 16 italic')
l2 = Label(window, text="섭씨", font = 'helevetica 16 italic')

l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

e1 = Entry(window, bg = "green", fg ="yellow")
e2 = Entry(window, bg = "green", fg ="yellow")
e1.grid(row=0, column =1)
e2.grid(row=1, column =1)

b1 = Button(window, text = "화씨->섭씨", command=process)
b2 = Button(window, text = "섭씨->화씨", font ='helvetica 12')
b1.grid(row=2, column =0)
b2.grid(row=2, column =1)


window.mainloop()
