from morse_code_dict import morse
import tkinter as tk
import threading



class MorseConverter:

    def convert(self):
        self.converting = True
        self.morse_text.config(state="normal")
        normal_text = self.normal_text.get("1.0", "end")

        text = ""
        for i in normal_text[:-1]:
            i = i.upper()
            if i in morse:
                temp = str.translate(i, self.transTAB)
                text += temp
            else:
                print(len(self.normal_text.get("1.0", "end")))
                self.normal_text.delete("1.0", "end")
                self.normal_text.insert("1.0", normal_text[:-2])
                print(len(self.normal_text.get("1.0", "end")))


        self.morse_text.delete("1.0", 'end')
        self.morse_text.insert("1.0", text)

        self.morse_text.config(state="disabled")
        self.converting = False

    def Create_widgets(self):
        main_frame = tk.Frame(self.root, bg='#cec1ff')
        main_frame.pack()

        head_label = tk.Label(main_frame, font='Times 30', text="Welcome to Morse code converter!", bg='#cec1ff')
        head_label.grid(row=0, column=0, columnspan=2)

        normal_label = tk.Label(main_frame, font='Times 20', text="Enter normal\ntext here:", bg='#cec1ff')
        normal_label.grid(row=1, column=0)

        self.normal_text = tk.Text(main_frame, font="Times 14", height=5, width=50)
        self.normal_text.grid(row=1, column=1, pady=10, padx=20)
        self.normal_text.insert("1.0", "Type text here!")

        morse_label = tk.Label(main_frame, font='Times 20', text="Here is your\nmorse code:", bg='#cec1ff')
        morse_label.grid(row=2, column=0)

        self.morse_text = tk.Text(main_frame, font="Times 14", height=5, width=50)
        self.morse_text.grid(row=2, column=1, pady=10, padx=20)
        self.morse_text.config(state="disabled")

    def loop(self):
        normal_len = 0
        while not self.converting:
            if len(self.normal_text.get("1.0", 'end')) != normal_len:
                normal_len = len(self.normal_text.get("1.0", "end"))

                self.convert()

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Morse code")
        self.root.resizable(False, False)
        self.root.configure(bg='#cec1ff')
        self.Create_widgets()

        # test = "Hello World"

        self.transTAB = str.maketrans(morse)
        self.converting = False

        self.thread = threading.Thread(target=self.loop)
        self.thread.setDaemon(True)

        self.thread.start()

        self.root.mainloop()


if __name__ == '__main__':
    MorseConverter()
