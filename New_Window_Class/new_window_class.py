import tkinter as tk
from tkinter import *


class NewWindow:

    def __init__(self, window_title, bg, is_resizable):
        self.window_title = window_title
        self.bg = bg
        self.is_resizable = is_resizable
        self.master = tk.Tk()
        print(str(self.master))
        self.master.title(str(window_title))
        self.master.config(bg=bg)
        self.master.resizable(is_resizable, is_resizable)

    def add_label(self, text, font, text_color, bg, grid_row, grid_column):
        label = tk.Label(font=font, text=text, fg=text_color, bg=bg)
        label.grid(row=grid_row, column=grid_column)

    def add_button(self, text, font, text_color, bg, grid_row, grid_column, command):
        button = tk.Button(font=font, text=text, fg=text_color, bg=bg, command=command)
        button.grid(row=grid_row, column=grid_column)


def clicked():
    quit()


win1 = NewWindow("Window Title", 'black', False)
win1.add_label("VERY COOL LABEL TEXT", "Times 20", 'blue', 'purple', 0, 0)
win1.add_label("VERY TESTY LABEL", "Times 20", 'yellow', 'white', 1, 0)
win1.add_button('Very cool\nquit button', 'Times 12', 'green', 'white', 2, 1, clicked)

win1.master.mainloop()
