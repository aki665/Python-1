import tkinter as tk
from tkinter import StringVar, ttk
import math
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy


class Graph:
    def update_line(self, function, ax, functions_id):
        line = ax.lines[functions_id]
        print("UPDATING LINE: ", line)
        temp = function.calculate()
        line.set_data(temp[0], temp[1])
        self.canvas.draw()

    def add_line(self, function, ax, functions_id):
        print("add_line FunctionBarOBJ and ID", function, functions_id)
        self.functions_list.append(function)
        temp = function.calculate()
        print("Result from calculation: ", temp[1])

        ax.plot(temp[0], temp[1])

        temp2 = ax.lines[functions_id]
        print("LINE and ID: ", temp2, functions_id)
        function.get_line(temp2)
        print("AX.LINES:", ax.lines)
        #help(ax.lines[0])
        #help(ax.plot)

    def delete_line(self, line, id):
        print(line, id)
        line.remove()
        self.functions_list.pop(id)
        temp = 0
        for i in self.functions_list:
            i.id = temp
            print(i.id)
            temp += 1


    def __init__(self, f, root):
        self.canvas = FigureCanvasTkAgg(f, root)
        self.canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True)
        self.functions_list = []


class FunctionBar:
    def get_line(self, line):
        self.line = line


    def update_line(self):
        #self.window.functions_amount -= 1
        #Graph.delete_line(self.line)
        self.window.update_line(self, self.window.ax, self.id)

    def calculate(self):
        #print("A, B, C and D: ", self.a, self.b, self.c, self.d)
        x = []
        y = []
        #print("inside calculate ", self.degree.get())
        if self.degree.get() == "First degree":  # 2x - 1     a=2, b=1
            for i in range(- self.window.x_lim, self.window.x_lim + 1):
                x.append(i)
                j = self.a * i - self.b
                y.append(j)

        if self.degree.get() == "Second degree": #2x^2 - 5x - 5
            for i in numpy.arange(- self.window.x_lim, self.window.x_lim + 1, 0.1):
                x.append(i)
                j = self.a * i * i - self.b * i - self.c
                y.append(j)
        if self.degree.get() == "Third degree": #2x^3 - 5x^2 -4x - 5
            for i in numpy.arange(- self.window.x_lim, self.window.x_lim + 1, 0.1):
                x.append(i)
                j = self.a * i * i * i - self.b * i * i - self.c * i - self.d
                y.append(j)

        temp = [x, y]
        return temp

    def drop_down(self, degree, firsttime = False):
        frame = self.function
        if degree == "First degree":
            self.first_degree(frame)
        elif degree == "Second degree":
            self.second_degree(frame)
        elif degree == "Third degree":
            self.third_degree(frame)

        if firsttime is False:
            self.update_line()

    def first_degree(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        fx = tk.Label(frame, text="f(x) = ", font="Times 12")
        fx.grid(column=0, row=0)

        entry1 = tk.Entry(frame, width=3, text=self.a_text)
        entry1.grid(column=1, row=0)

        x1_label = tk.Label(frame, text="x - ", font="Times 10")
        x1_label.grid(column=2, row=0)

        entry2 = tk.Entry(frame, width=3, text=self.b_text)
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
        self.window.delete_line(self.line, self.id)
        self.window.functions_id -= 1

    def __init__(self, GraphWindow, frame, root, id):
        self.window = GraphWindow
        print("ID in __init__: ", id)
        self.id = id
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
        self.drop_down(options_list[0], firsttime=True)

        delete_button = ttk.Button(self.functions, text='-', command=lambda: self.delete())
        delete_button.pack(side='right')


class GraphWindow(Graph, FunctionBar):

    def new_function(self):
        self.functions_id += 1
        temp = FunctionBar(self, self.functions_frame, self.root, self.functions_id)
        Graph.add_line(self, temp, self.ax, self.functions_id)


    def create_widgets(self):
        window_frame = tk.Frame(self.root)
        window_frame.pack()

        top_label = tk.Label(window_frame, font="Times 20", text="Graph your functions here!")
        top_label.pack()

        self.functions_frame = tk.Frame(window_frame)
        self.functions_frame.pack(side='bottom')

        # self.graph = Graph(self.f, self.root)

        add_button = ttk.Button(self.functions_frame, text='Add function', command=lambda: self.new_function())
        add_button.pack(side='right')

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Function Graphing")
        self.f = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.f.add_subplot()
        #self.ax.set_ylabel("Y axis")
        #self.ax.set_xlabel("X axis")
        self.ax.grid()
        self.ax.set_ylim((-10, 10))
        self.x_lim = 10
        self.ax.set_xlim(- self.x_lim, self.x_lim)
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')

        self.functions_id = -1
        self.function_list = []
        self.create_widgets()
        super().__init__(self.f, self.root)
        self.new_function()

        self.root.mainloop()




if __name__ == "__main__":
    GraphWindow()
