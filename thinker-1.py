from tkinter import *

window = Tk()

button = Button(window, text = "클릭하세요!") #윈도우에 버튼 추가 
button.pack()

window.mainloop()

#윈도우 배치 관리자

from tkinter import *

window = Tk()
w = Label(window,text="박스 #1", bg = "red", fg="white")
w.place(x=0,y=0)
w = Label(window,text="박스 #2", bg = "green", fg="black")
w.place(x=20,y=20)
w = Label(window,text="박스 #3", bg = "blue", fg="white")
w.place(x=40,y=40)
window.mainloop()

#격자배치관리자

from tkinter import *

window = Tk()

l1 = Label(window, text = "화씨")
l2 = Label(window, text = "섭씨")
l1.grid(row=0, column = 0)
l2.grid(row=1, column = 0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Button(window, text = "화씨 -> 섭씨")
b2 = Button(window, text = "섭씨 -> 화씨 ")
b1.grid(row=2, column = 0)
b2.grid(row=2,column = 1)


window.mainloop()




