#importing all modules from tkinter library
from tkinter import *

#to creat a window
window = Tk()

#to creat title of a window
window.title("A SIMPLE CALCULATOR")

#dimensions of window
window.geometry("420x590")
window.resizable(False,False)

# to set background color of window
window.config(background="black")

equation =""

def show(value):
    global equation
    equation+=value
    label.config(text=equation)

def clear():
    global equation
    equation=""
    label.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label.config(text=result)

#to create a label in the window
label = Label(window,width=20,height=2,text="",font=("times new roman",30))
label.pack()
#to create first line in window
#to create buttons for calculator
button_clear = Button(window,text="c",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="#beeb1c",
                command=lambda:clear())

#to place a button in window
button_clear.place(x=15,y=100)
button_div = Button(window,text="/",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda:show("/"))
button_div.place(x=118,y=100)
button_remainder = Button(window,text="%",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("%"))
button_remainder.place(x=222,y=100)
button_mul = Button(window,text="*",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("*"))
button_mul.place(x=325,y=100)

#to create second line in window
button_7 = Button(window,text="7",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("7"))
button_7.place(x=15,y=200)
button_8 = Button(window,text="8",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("8"))
button_8.place(x=118,y=200)
button_9 = Button(window,text="9",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("9"))
button_9.place(x=222,y=200)
button_sub = Button(window,text="-",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("-"))
button_sub.place(x=325,y=200)

#to create third line in window
button_4 = Button(window,text="4",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("4"))
button_4.place(x=15,y=300)
button_5 = Button(window,text="5",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("5"))
button_5.place(x=118,y=300)
button_6 = Button(window,text="6",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("6"))
button_6.place(x=222,y=300)
button_add = Button(window,text="+",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("+"))
button_add.place(x=325,y=300)

#to create fourth line i window
button_1 = Button(window,text="1",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("1"))
button_1.place(x=15,y=400)
button_2 = Button(window,text="2",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("2"))
button_2.place(x=118,y=400)
button_3 = Button(window,text="3",width=3,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("3"))
button_3.place(x=222,y=400)

#to create fifth line in window
button_0 = Button(window,text="0",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("0"))
button_0.place(x=15,y=500)

button_point = Button(window,text=".",width=5,height=1,font=("arial",30,"bold"),bd=5,fg="black",bg="grey",
                command=lambda: show("."))
button_point.place(x=172,y=500)
button_calc = Button(window,text="=",width=3,height=3,font=("arial",30,"bold"),bd=7,fg="black",bg="#50b3cc",
                command=lambda:calculate())
button_calc.place(x=325,y=400)

window.mainloop()
