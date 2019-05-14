import tkinter
from tkinter import *

top = tkinter.Tk()
# top.geometry("250x280+0+0")
top.title('Calculator')
top.resizable(False, False)
num1 = IntVar()
num2 = IntVar()
op = StringVar()

num_text = Label(anchor=E, height=1)
num_text.config(font=("Times", 24))
num_text.grid(columnspan=5, sticky=E)


def checkOverflow():
    if result.get() > 99999999999:
        screen.set(0)
        setDisplay(0)
        num_text.config(text="OverFlow")


def setDisplay(number):
    num_text.config(text=str(number))


def onclick(a):
    if len(str(screen.get())) < 8:

        if screen.get() == result.get():
            clearDisplay()
        if screen.get() == 0:
            screen.set(a)
            setDisplay(a)
        else:
            b = screen.get()
            screen.set(str(b) + str(a))
            setDisplay(screen.get())
    else:
        return


def clearDisplay():
    screen.set(0)
    setDisplay(0)


def disableButtons():
    Button_add.config(state=DISABLED)
    Button_sub.config(state=DISABLED)
    Button_mult.config(state=DISABLED)
    Button_div.config(state=DISABLED)


def enableButtons():
    Button_add.config(state='normal')
    Button_sub.config(state='normal')
    Button_mult.config(state='normal')
    Button_div.config(state='normal')


def setOperation(operation):
    op.set(operation)

    if op.get() == "+":
        num1.set(screen.get())
        clearDisplay()
        disableButtons()

    if op.get() == "-":
        num1.set(screen.get())
        clearDisplay()
        disableButtons()

    if op.get() == "*":
        num1.set(screen.get())
        clearDisplay()
        disableButtons()

    if op.get() == "/":
        num1.set(screen.get())
        clearDisplay()
        disableButtons()


def Calculate():
    if op.get() == "+":
        num2.set(screen.get())
        result.set(num1.get() + num2.get())
        screen.set(result.get())
        setDisplay(result.get())
        checkOverflow()
        enableButtons()

    if op.get() == "-":
        num2.set(screen.get())
        result.set(num1.get() - num2.get())
        screen.set(result.get())
        setDisplay(result.get())
        checkOverflow()
        enableButtons()

    if op.get() == "*":
        num2.set(screen.get())
        result.set(num1.get() * num2.get())
        screen.set(result.get())
        setDisplay(result.get())
        checkOverflow()
        enableButtons()

    if op.get() == "/":
        num2.set(screen.get())
        result.set(num1.get() / num2.get())
        screen.set(result.get())
        setDisplay(result.get())
        checkOverflow()
        enableButtons()


result = IntVar()
screen = IntVar()
screen.set(0)
setDisplay(0)
num2.set(0)

Padx = 15
Pady = 15
Button_num1 = tkinter.Button(top, text='1', padx=Padx, pady=Pady, command=lambda: onclick(1))
Button_num1.grid(row=4, column=0, sticky=W)

Button_num2 = tkinter.Button(top, text='2', padx=Padx, pady=Pady, command=lambda: onclick(2))
Button_num2.grid(row=4, column=1, sticky=W)

Button_num3 = tkinter.Button(top, text='3', padx=Padx, pady=Pady, command=lambda: onclick(3))
Button_num3.grid(row=4, column=2, sticky=W)

Button_num4 = tkinter.Button(top, text='4', padx=Padx, pady=Pady, command=lambda: onclick(4))
Button_num4.grid(row=3, column=0, sticky=W)

Button_num5 = tkinter.Button(top, text='5', padx=Padx, pady=Pady, command=lambda: onclick(5))
Button_num5.grid(row=3, column=1, sticky=W)

Button_num6 = tkinter.Button(top, text='6', padx=Padx, pady=Pady, command=lambda: onclick(6))
Button_num6.grid(row=3, column=2, sticky=W)

Button_num7 = tkinter.Button(top, text='7', padx=Padx, pady=Pady, command=lambda: onclick(7))
Button_num7.grid(row=2, column=0, sticky=W)

Button_num8 = tkinter.Button(top, text='8', padx=Padx, pady=Pady, command=lambda: onclick(8))
Button_num8.grid(row=2, column=1, sticky=W)

Button_num9 = tkinter.Button(top, text='9', padx=Padx, pady=Pady, command=lambda: onclick(9))
Button_num9.grid(row=2, column=2, sticky=W)

Button_num0 = tkinter.Button(top, text='0', padx=Padx * 2 + 8, pady=Pady, command=lambda: onclick(0))
Button_num0.grid(row=5, column=0, columnspan=2, sticky=E)

Button_add = tkinter.Button(top, text='+', padx=Padx, pady=Pady * 2 + 14, command=lambda: setOperation("+"))
Button_add.grid(row=2, column=3, rowspan=2, sticky=W)

Button_sub = tkinter.Button(top, text='-', padx=Padx, pady=Pady, command=lambda: setOperation("-"))
Button_sub.grid(row=1, column=3, sticky=W)

Button_mult = tkinter.Button(top, text='*', padx=Padx, pady=Pady, command=lambda: setOperation("*"))
Button_mult.grid(row=1, column=2, sticky=W)

Button_div = tkinter.Button(top, text='/', padx=Padx, pady=Pady, command=lambda: setOperation("/"))
Button_div.grid(row=1, column=1, sticky=W)

Button_eq = tkinter.Button(top, text='=', padx=Padx, pady=Pady, command=lambda: Calculate())
Button_eq.grid(row=4, column=3, sticky=W)

Button_clear = tkinter.Button(top, text='CLEAR', padx=Padx * 2 - 6, pady=Pady, command=lambda: clearDisplay())
Button_clear.grid(row=5, column=2, columnspan=2, sticky=W)


top.mainloop()