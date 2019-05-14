import tkinter
from tkinter import *
from tkinter import ttk
import random
import time

score_list = []
question_num_list = []
operator_list = ['+', '-', '*', '/']
progbar_value = 0

total_question = 5
timevar = 10
score_label = tkinter.Label
entry = tkinter.Entry
start_button = tkinter.Button

def disable_event():
    pass


def Results_window(main):
    result = tkinter.Tk()
    result.geometry("+700+400")
    result.resizable(False, False)
    result.title('Results')

    corr_answ = 0
    for x in score_list:
        corr_answ = corr_answ + int(x)

    corr_pros = round((corr_answ / total_question * 100), 2)
    incorr_pros = round(((total_question - corr_answ) / total_question * 100), 2)

    print('Correct answers ' + str(corr_answ))
    result_label_text = 'You got ' + str(corr_answ) + ' out of ' + str(total_question) + ' correct!'

    result_label = tkinter.Label(result, font='Times 18', text=result_label_text)
    result_label.grid(row=0, column=0, columnspan=2)

    corr_result_bar = ttk.Progressbar(result, orient='vertical', length=80, maximum=total_question, value=corr_answ)
    corr_result_bar.grid(row=1, column=0)

    corr_result_label = tkinter.Label(result, font='Times 10', text='Correct:\n' + str(corr_pros) + '%')
    corr_result_label.grid(row=2, column=0)

    incorr_result_bar = ttk.Progressbar(result, orient='vertical', length=80, maximum=total_question,
                                        value=(total_question - corr_answ))
    incorr_result_bar.grid(row=1, column=1)

    incorr_result_label = tkinter.Label(result, font='Times 10', text='Incorrect:\n' + str(incorr_pros) + '%')
    incorr_result_label.grid(row=2, column=1)

    but_done = tkinter.Button(result, font='Times 12', text="Done", command=lambda: destroy_result(main))
    but_done.grid(row=3, column=1, sticky='e')

    while len(score_list) > 0:
        for a in score_list:
            print('Removing scores ' + str(score_list))
            score_list.remove(a)

    def destroy_result(main):
        start_button.config(main, state='normal')
        result.destroy()


    result.mainloop()


def question_generator():
    question_num_list = []
    operator = random.choice(operator_list)
    if operator == '/':
        num1 = random.randint(2, 100)
        numlist = []
        for x in range(1, num1):
            if num1 % x == 0 and x > 1:
                numlist.append(x)
        if len(numlist) > 0:
            num2 = random.choice(numlist)
        else:
            num2 = num1
        corr_result = int(num1 / num2)

    elif operator == '*':
        num1 = random.randint(2, 20)
        num2 = random.randint(2, 20)
        corr_result = int(num1 * num2)

    elif operator == '+':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        corr_result = int(num1 + num2)

    elif operator == '-':
        num1 = random.randint(2, 200)
        numlist = []
        for x in range(1, num1):
            numlist.append(x)
        num2 = random.choice(numlist)
        corr_result = int(num1 - num2)

    print(str(num1) + operator + str(num2) + '=' + str(corr_result))
    question_num_list.append(num1)
    question_num_list.append(operator)
    question_num_list.append(num2)
    question_num_list.append(corr_result)

    print(question_num_list)
    return question_num_list


def Create_question_window(window_number, main):
    start_button.config(main, state=DISABLED)





    def check_if_correct():

        time_left_bar.stop()

        print('Button pressed')
        if entry.get() == str(quest[3]):
            print('correct')
            score_list.append(1)
            print('correct answer, score list' + str(score_list))
            window_number.destroy()
            if len(score_list) < total_question:
                Create_question_window(2)
            else:
                Results_window()

        else:
            print('incorrect')
            score_list.append(0)
            print('Incorrect answer, score list' + str(score_list))
            window_number.destroy()
            if len(score_list) < total_question:
                Create_question_window(2)
            elif len(score_list) == total_question:
                print(score_list)

                Results_window()


    quest = question_generator()

    question = ("What is: " + str(quest[0]) + quest[1] + str(quest[2]) + " ?")
    # correct_result=quest[3]

    window_number = tkinter.Tk()
    window_number.geometry("+800+400")
    window_number.resizable(False, False)
    window_number.title("Question")
    window_number.protocol("WM_DELETE_WINDOW", disable_event)
    window_number.lift()
    window_number.focus_force()

    quest_label = tkinter.Label(window_number, font='Times 25', text=question)
    quest_label.grid(row=0, column=0, columnspan=2)

    answ_label = tkinter.Label(window_number, font='Times 20', text="Answer:")
    answ_label.grid(row=1, column=0, sticky='E')

    entry = tkinter.Entry(window_number, font='Times 20', width=5)
    entry.grid(row=1, column=1, sticky='W')
    entry.focus_force()

    submit_button = tkinter.Button(window_number, font='Times 12', text='Submit', command=lambda: check_if_correct())
    submit_button.grid(row=2, column=1, sticky='')

    entry.bind('<Return>', lambda event: check_if_correct())

    def timer():
        progbar_value = 0
        while progbar_value < (timevar * 10):
            progbar_value += 1
            window_number.update()
            time_left_bar.step(1)
            window_number.update()
            time.sleep(timevar / 100)
            if progbar_value == (timevar * 10):
                progbar_value = 0
                entry.delete(0, 'end')
                check_if_correct()
                break


    time_left_bar = ttk.Progressbar(window_number, orient='horizontal', length=100, maximum=timevar * 10,
                                    value=progbar_value)
    time_left_bar.grid(row=2, column=0, columnspan=2, sticky='w')
    timer()

    window_number.mainloop()


def Main_Window():
    def settings():
        def set_settings():
            global total_question
            total_question = int(entry_one.get())
            global timevar
            timevar = int(entry_two.get())

            settings.destroy()

        settings = tkinter.Tk()
        settings.geometry("+600+400")
        # settings.protocol("WM_DELETE_WINDOW", disable_event)
        settings.title('Settings')
        settings.resizable(False, False)

        label_one = tkinter.Label(settings, font='Times 15', text="Question amount:")
        label_one.grid(row=0, column=0, columnspan=2)
        entry_one = tkinter.Entry(settings, font='times 15', width=5)
        entry_one.grid(row=0, column=2)
        entry_one.insert(0, str(total_question))

        label_two = tkinter.Label(settings, font='Times 15', text="Answer time (sec):")
        label_two.grid(row=1, column=0, columnspan=2)
        entry_two = tkinter.Entry(settings, font='times 15', width=5, text=str(total_question))
        entry_two.grid(row=1, column=2)
        entry_two.insert(0, timevar)

        but_one = tkinter.Button(settings, font='Times 12', text="OK", command=lambda: set_settings())
        but_one.grid(row=2, column=2)
        settings.mainloop()

    main = tkinter.Tk()
    main.geometry("+600+400")
    main.protocol("WM_DELETE_WINDOW", disable_event)
    main.title('Math Question Game')
    main.resizable(False, False)

    main_label = tkinter.Label(main, font='Times 20', text='Welcome to math question game!')
    main_label.grid(row=0, column=0, columnspan=3)

    start_button = tkinter.Button(main, font='Times 12', text='Start\nGame', command=lambda: Create_question_window(5,main))
    start_button.grid(row=1, column=0, sticky='e')

    quit_button = tkinter.Button(main, font='Times 12', text='Quit', command=lambda: main.destroy(), pady=10)
    quit_button.grid(row=1, column=2, sticky='w')

    menubar = tkinter.Menu(main)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=filemenu)
    filemenu.add_command(label="Settings", command=settings)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=main.destroy)

    main.config(menu=menubar)
    main.mainloop()


Main_Window()
