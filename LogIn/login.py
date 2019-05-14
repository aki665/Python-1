import tkinter as tk
from tkinter import StringVar, messagebox


class LogInWindow:

    def Login(self):
        self.file = open("Account_Information.txt", "r")
        line = self.file.readlines()
        for i in line:
            if i == '\n':
                pass
            else:
                split = i.split(",")
                if split[0] == self.name_entry.get() and split[1][1:-1] == self.password_entry.get():
                    messagebox.showinfo('Successful', 'You are now logged in!!!')
                    return
                else:
                    pass

        messagebox.showerror('Error', 'Incorrect Username or Password')

    def Signin(self):
        self.top_text.set('Enter your desired\nname and password')

        self.frame1.pack_forget()
        self.frame2.pack(fill='both')

    def CreateAccount(self):
        self.error_name_label.grid_forget()
        self.error_password_label.grid_forget()
        if len(self.new_name_entry.get()) < 3:

            self.error_name_label.grid(row=1, column=1)

        elif len(self.password2_entry.get()) < 4:
            self.error_password_text.set('Password is too short!')
            self.error_password_label.grid(row=3, column=1)

        elif self.password2_entry.get() != self.password_check_entry.get():
            self.error_password_text.set('Passwords are not the same!')
            self.error_password_label.grid(row=3, column=1)

        elif self.password2_entry.get() == self.password_check_entry.get():
            self.file = open("Account_Information.txt", "a")

            new_account_text = '\n' + self.new_name_entry.get() + ',' + ' ' + self.password2_entry.get() + '\n'
            self.file.write(new_account_text)
            self.file.close()

            self.top_text.set('Please Log In')
            self.frame2.pack_forget()
            self.frame1.pack(fill='both')

    def back(self):
        self.top_text.set('Please Log In')
        self.error_password_label.grid_forget()
        self.error_name_label.grid_forget()
        self.frame2.pack_forget()
        self.frame1.pack(fill='both')

    def Create_widgets(self):
        top_label = tk.Label(textvariable=self.top_text, font=('Times 20'), bg='white')
        top_label.pack()

        self.frame1 = tk.Frame(bg='white')
        self.frame1.pack(expand=1)

        name_label = tk.Label(self.frame1, text='Name', font='Times 12', bg='white', anchor='e', padx=60)
        name_label.grid(row=0, column=0, sticky='W')

        self.name_entry = tk.Entry(self.frame1, font='Times 12')
        self.name_entry.grid(row=0, column=1, columnspan=2)

        password_label = tk.Label(self.frame1, text='Password', font='Times 12', bg='white', anchor='w', padx=50)
        password_label.grid(row=1, column=0)

        self.password_entry = tk.Entry(self.frame1, show="*", font='Times 12')
        self.password_entry.grid(row=1, column=1, columnspan=2)

        login_button = tk.Button(self.frame1, text='Log In', command=lambda: self.Login())
        login_button.grid(row=2, column=2, sticky='e')

        exit_button = tk.Button(self.frame1, text='Exit', command=lambda: self.root.destroy())
        exit_button.grid(row=2, column=3)

        signin_button = tk.Button(self.frame1, text='Sign In', command=lambda: self.Signin())
        signin_button.grid(row=2, column=0, columnspan=2, sticky='e')

        self.frame2 = tk.Frame(bg='white')

        name_label = tk.Label(self.frame2, text='Name', font='Times 12', bg='white', anchor='w', padx=70)
        name_label.grid(row=0, column=0)

        self.new_name_entry = tk.Entry(self.frame2, font='Times 12')
        self.new_name_entry.grid(row=0, column=1, columnspan=2)

        password_label = tk.Label(self.frame2, text='Password', font='Times 12', bg='white', anchor='w', padx=10)
        password_label.grid(row=2, column=0)

        self.password2_entry = tk.Entry(self.frame2, show="*", font='Times 12')
        self.password2_entry.grid(row=2, column=1, columnspan=2)

        password_check_label = tk.Label(self.frame2, text='Password again', font='Times 12', bg='white', anchor='w',
                                        padx=10)
        password_check_label.grid(row=4, column=0)

        self.password_check_entry = tk.Entry(self.frame2, show="*", font='Times 12')
        self.password_check_entry.grid(row=4, column=1, columnspan=2)

        self.error_name_label = tk.Label(self.frame2, text='Name is too short!', bg='white', fg='red', font='Times 8')
        self.error_name_label.grid_forget()

        self.error_password_label = tk.Label(self.frame2, textvariable=self.error_password_text, bg='white', fg='red',
                                             font='Times 8')
        self.error_password_label.grid_forget()

        create_account_button = tk.Button(self.frame2, text='Create Account', command=lambda: self.CreateAccount())
        create_account_button.grid(row=5, column=2, sticky='e')

        back_button = tk.Button(self.frame2, text='Back', command=lambda: self.back())
        back_button.grid(row=5, column=3)

    def __init__(self):
        try:
            self.file = open("Account_Information.txt", "r")
            f1 = self.file.readlines()
            for line in f1:
                if line[:-1] == 'Admin, Admin':
                    self.file.close()
                    break
            else:
                self.file = open("Account_Information.txt", "a")
                self.file.write('\n' + "Admin, Admin\n")
                self.file.close()

        except FileNotFoundError:
            self.file = open("Account_Information.txt", "w+")
            self.file.write('Admin, Admin\n')
            self.file.close()

        self.root = tk.Tk()

        self.root.title('Log In Test')
        self.root.config(bg='white')
        self.root.resizable(False, False)
        self.top_text = StringVar()
        self.top_text.set('Please Log In')
        self.frame1 = tk.Frame
        self.name_entry = tk.Entry
        self.password_entry = tk.Entry
        self.frame2 = tk.Frame
        self.error_password_label = tk.Label
        self.error_password_text = StringVar()
        self.error_name_label = tk.Label
        self.password2_entry = tk.Entry
        self.password_check_entry = tk.Entry
        self.new_name_entry = tk.Entry
        self.Create_widgets()

        self.root.mainloop()


if __name__ == '__main__':
    LogInWindow()
