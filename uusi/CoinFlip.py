import random
import tkinter
import time
from tkinter import *
from tkinter import ttk


def welcome_text():
    welcome = Label(msg, height=1, text=text.get(), font=("Times", 15))
    welcome.grid(row=0, column=1, columnspan=3)


def start():
    for x in range(0, 101):
        prgb.config(value=x)
        time.sleep(0.05)
        prgb.update()
    else:
        msg.destroy()


def disable_event_msg():
    pass


def create_widgets():
    heads.set("Heads %: \n" + str(head.get()))
    tails.set("Tails %: \n" + str(tail.get()))

    welcome_text = Label(top, height=1, text='Welcome to coin flip simulator', font=("Times", 20))
    welcome_text.grid(row=0, column=0, columnspan=3)

    heads_text = Label(top, height=2, font=("Times", 10), text=heads.get())
    heads_text.grid(row=1, column=0)

    flip_button = Button(top, text='Flip a coin', command=lambda: flip())
    flip_button.grid(row=1, column=1)

    tails_text = Label(top, height=2, font=("Times", 10), text=tails.get())
    tails_text.grid(row=1, column=2)

    total_flips = Label(top, font=("Times", 15))
    total_flips.config(text="Total flips: " + total.get())
    total_flips.grid(row=2, column=0, columnspan=3)


def flip():
    total.set(str(int(total.get()) + 1))
    total_flips = float(total.get())

    if random.choice(coin) == 'Head':
        total_heads.set(total_heads.get() + 1)


    else:
        total_tails.set(total_tails.get() + 1)

    result_heads = (total_heads.get() / total_flips * 100)
    result_tails = (total_tails.get() / total_flips * 100)

    tail.set(str(round(result_tails, 2)))
    head.set(str(round(result_heads, 2)))

    top.after(0, create_widgets())


msg = tkinter.Tk()

text = StringVar()
text.set('Please wait while we load the Coin Flip Simulator')
msg.title('Coin Flip')
msg.resizable(False, False)

welcome_text()

prgb = ttk.Progressbar(msg, orient=HORIZONTAL, length=400)
prgb.config(mode='determinate', maximum=100, value=0)
prgb.grid(row=1, column=1, columnspan=3)

msg.protocol('WM_DELETE_WINDOW', disable_event_msg)
start()
msg.mainloop()

top = tkinter.Tk()
top.title('Coin Flip')
top.resizable(False, False)

coin = ['Head', 'Tail']
heads = StringVar()
tails = StringVar()
total = StringVar()
tail = StringVar()
head = StringVar()
total_heads = IntVar()
total_tails = IntVar()

tail.set(0)
head.set(0)
total.set(0)
total_heads.set(0)
total_tails.set(0)

create_widgets()

top.mainloop()
