import tkinter as tk
from tkinter import StringVar, ttk
import math
import random
import matplotlib.pyplot as plt
# plt.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import time


class Graph:
    @staticmethod
    def add_line(function_list, f):
        for functions in function_list:
            print(functions.calculate())
            temp2 = functions.calculate()
            g = f.add_subplot()
            g.plot(temp2)
            # help(g.plot)
        return function_list

    @staticmethod
    def delete_line():
        pass

    def __init__(self, f, root):
        canvas = FigureCanvasTkAgg(f, root)
        canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True)


class FunctionBar():
    def calculate(self):
        # x = []
        y = []
        print("inside calculate ", self.degree.get())
        if self.degree.get() == "First degree":  # 2x - 1     a=2, b=1
            for i in range(10):
                # x.append(i)
                j = self.a * i - self.b
                y.append(j)

        return y

    def drop_down(self, degree):
        frame = self.function
        if degree == "First degree":
            self.first_degree(frame)
        elif degree == "Second degree":
            self.second_degree(frame)
        elif degree == "Third degree":
            self.third_degree(frame)

    def first_degree(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        fx = tk.Label(frame, text="f(x) = ", font="Times 12")
        fx.grid(column=0, row=0)

        entry1 = tk.Entry(frame, width=3, text=self.a_text)
        entry1.grid(column=1, row=0)

        x1_label = tk.Label(frame, text="x - ", font="Times 10")
        x1_label.grid(column=2, row=0)

        entry2 = tk.Entry(frame, width=3, text=self.c_text)
        entry2.grid(column=5, row=0)

    def second_degree(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        fx = tk.Label(frame, text="f(x) = ", font="Times 12")
        fx.grid(column=0, row=0)

        entry1 = tk.Entry(frame, width=3, text=self.a_text)
        entry1.grid(column=1, row=0)

        x1_label = tk.Label(frame, text="x² - ", font="Times 10")
        x1_label.grid(column=2, row=0)

        entry2 = tk.Entry(frame, width=3, text=self.b_text)
        entry2.grid(column=3, row=0)

        x2_label = tk.Label(frame, text="x - ", font="Times 10")
        x2_label.grid(column=4, row=0)

        entry3 = tk.Entry(frame, width=3, text=self.c_text)
        entry3.grid(column=5, row=0)

    def third_degree(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        fx = tk.Label(frame, text="f(x) = ", font="Times 12")
        fx.grid(column=0, row=0)

        entry1 = tk.Entry(frame, width=3, text=self.a_text)
        entry1.grid(column=1, row=0)

        x1_label = tk.Label(frame, text="x³ - ", font="Times 10")
        x1_label.grid(column=2, row=0)

        entry2 = tk.Entry(frame, width=3, text=self.b_text)
        entry2.grid(column=3, row=0)

        x2_label = tk.Label(frame, text="x² - ", font="Times 10")
        x2_label.grid(column=4, row=0)

        entry3 = tk.Entry(frame, width=3, text=self.c_text)
        entry3.grid(column=5, row=0)

        x3_label = tk.Label(frame, text="x - ", font="Times 10")
        x3_label.grid(column=6, row=0)

        entry4 = tk.Entry(frame, width=3, text=self.d_text)
        entry4.grid(column=7, row=0)

    def delete(self):
        self.functions.destroy()
        Graph.delete_line()

    def __init__(self, frame, root):
        self.a = random.randint(-5, 5)
        self.b = random.randint(1, 10)
        self.c = random.randint(1, 10)
        self.d = random.randint(1, 10)
        self.a_text = StringVar(root)
        self.b_text = StringVar(root)
        self.c_text = StringVar(root)
        self.d_text = StringVar(root)
        self.a_text.set(self.a)
        self.b_text.set(self.b)
        self.c_text.set(self.c)
        self.d_text.set(self.d)
        self.degree = StringVar(root)
        colors = ["blue", "yellow", "black", "purple", "red", "green"]
        self.functions = tk.Frame(frame, bg=random.choice(colors))
        self.functions.pack(side='bottom')
        self.function = tk.Frame(self.functions, bg='yellow')
        self.function.pack(side='left', padx=40, pady=10)

        options_list = ["First degree", "Second degree", "Third degree"]
        options = ttk.OptionMenu(self.functions, self.degree, options_list[0], *options_list, command=self.drop_down)
        options.pack(side='right', padx=50)
        self.drop_down("First degree")

        delete_button = ttk.Button(self.functions, text='-', command=lambda: self.delete())
        delete_button.pack(side='right')


class GraphWindow:
    def new_function(self):
        self.functions += 1
        temp = FunctionBar(self.functions_frame, self.root)
        self.function_list.append(temp)

        self.function_list = Graph.add_line(self.function_list, self.f)
        print(self.function_list)

    def create_widgets(self):
        window_frame = tk.Frame(self.root)
        window_frame.pack()

        top_label = tk.Label(window_frame, font="Times 20", text="Graph your functions here!")
        top_label.pack()

        self.functions_frame = tk.Frame(window_frame)
        self.functions_frame.pack(side='bottom')

        Graph(self.f, self.root)

        add_button = ttk.Button(self.functions_frame, text='Add function', command=lambda: self.new_function())
        add_button.pack(side='right')

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Function Graphing")
        self.f = Figure(figsize=(5, 5), dpi=100)
        print(self.f)
        self.functions = 0
        self.function_list = []
        self.create_widgets()
        self.new_function()
        self.root.mainloop()


if __name__ == "__main__":
    GraphWindow()
