from tkinter import *

def open():
    pass


def quit():
    window.quit()


window = Tk()

menubar = Menu(window)
filemenu = Menu(menubar)

filemenu.add_command(label="열기",command=open)
filemenu.add_command(label="종료",command=quit)

menubar.add_cascade(label="파일", menu = filemenu)


window.config(menu=menubar)
window.mainloop()


#MyPaint 프로그램

from tkinter import *

def paint(event):
    x1,y1 = (event.x-1),(event.y+1)
    x2,y2 = (event.x-1),(event.y+1)
    canvas.create_oval(x1,y1,x2,y2)
    


window = Tk()

canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>", paint)
window.mainloop()
