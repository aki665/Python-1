import tkinter as tk
from tkinter import StringVar, messagebox
import TicTacToeAI
import time


class TicTacToe:



    def victory(self, player_number):
        self.board = [' '] * 10

        self.button1.configure(state='disabled')
        self.button2.configure(state='disabled')
        self.button3.configure(state='disabled')
        self.button4.configure(state='disabled')
        self.button5.configure(state='disabled')
        self.button6.configure(state='disabled')
        self.button7.configure(state='disabled')
        self.button8.configure(state='disabled')
        self.button9.configure(state='disabled')

        if player_number == 0:
            self.turn_text.set("It's a Tie!!!")

        elif player_number == 1:
            self.turn_text.set('%s WON!!!' % self.player1)

        elif player_number == 2:
            self.turn_text.set('%s WON!!!' % self.player2)

        msg_box = messagebox.askyesno(self.turn_text.get(), "Do you want to play again?")
        if msg_box:
            self.start_game()
        else:
            self.game_frame.pack_forget()
            self.turn_label.pack_forget()
            self.main_frame.pack(expand=1)

    def insert_to_board(self, board_place, x_or_o):
        if x_or_o == 'X':
            if board_place == 1:
                self.board[board_place-1] = 'X'
            elif board_place == 2:
                self.board[board_place-1] = 'X'
            elif board_place == 3:
                self.board[board_place-1] = 'X'
            elif board_place == 4:
                self.board[board_place-1] = 'X'
            elif board_place == 5:
                self.board[board_place-1] = 'X'
            elif board_place == 6:
                self.board[board_place-1] = 'X'
            elif board_place == 7:
                self.board[board_place-1] = 'X'
            elif board_place == 8:
                self.board[board_place-1] = 'X'
            elif board_place == 9:
                self.board[board_place-1] = 'X'


        elif x_or_o == 'O':

            if board_place == 1:
                self.board[board_place - 1] = 'O'
            elif board_place == 2:
                self.board[board_place - 1] = 'O'
            elif board_place == 3:
                self.board[board_place - 1] = 'O'
            elif board_place == 4:
                self.board[board_place-1] = 'O'
            elif board_place == 5:
                self.board[board_place-1] = 'O'
            elif board_place == 6:
                self.board[board_place-1] = 'O'
            elif board_place == 7:
                self.board[board_place-1] = 'O'
            elif board_place == 8:
                self.board[board_place-1] = 'O'
            elif board_place == 9:
                self.board[board_place-1] = 'O'

        #print(self.board)
    def activate_button(self, button_num):
        self.p1_turn = None

        if button_num - 1 == 0:
            print("AI presses Button1")
            self.button1.invoke()
        elif button_num - 1 == 1:
            print("AI presses Button2")
            self.button2.invoke()
        elif button_num - 1 == 2:
            print("AI presses Button3")
            self.button3.invoke()
        elif button_num - 1 == 3:
            print("AI presses Button4")
            self.button4.invoke()
        elif button_num - 1 == 4:
            print("AI presses Button5")
            self.button5.invoke()
        elif button_num - 1 == 5:
            print("AI presses Button6")
            self.button6.invoke()
        elif button_num - 1 == 6:
            print("AI presses Button7")
            self.button7.invoke()
        elif button_num - 1 == 7:
            print("AI presses Button8")
            self.button8.invoke()
        elif button_num - 1 == 8:
            print("AI presses Button9")
            self.button9.invoke()


    def on_click(self, button):
        temp = str(button)
        if temp[-1] is 'n':
            board_place = 1
        else:
            board_place = int(temp[-1])



        if self.p1_turn:
            turn_text = ("Its %s's turn!" % self.player2)
            self.turn_text.set(turn_text)
            button.configure(text='X')
            self.p1_turn = False
            button.configure(state='disabled')
            self.insert_to_board(board_place, 'X')
            self.root.update()
            self.check_win()


        elif not self.p1_turn and self.player2 != "AI":
            turn_text = ("Its %s's turn!" % self.player1)
            self.turn_text.set(turn_text)
            button.configure(text='O')
            self.p1_turn = True
            button.configure(state='disabled')
            self.insert_to_board(board_place, 'O')
            self.root.update()
            self.check_win()

        elif self.p1_turn is None:
            button.configure(text='O')
            turn_text = ("Its %s's turn!" % self.player1)
            self.turn_text.set(turn_text)
            self.p1_turn = True
            button.configure(state='disabled')
            self.insert_to_board(board_place, 'O')
            print(self.board)
            self.root.update()
            self.check_win()

        if self.player2 == 'AI' and not self.p1_turn:
            print("This goes in ", self.board)
            move = TicTacToeAI.getComputerMove(self.board)
            print("what was returned "+str(move))
            
            time.sleep(1)

            self.activate_button(move)
            self.root.update()


        


    def check_win(self):
        if (self.button1['text'] == 'X' and self.button2['text'] == 'X' and self.button3['text'] == 'X' or
                self.button4['text'] == 'X' and self.button5['text'] == 'X' and self.button6['text'] == 'X' or
                self.button7['text'] == 'X' and self.button8['text'] == 'X' and self.button9['text'] == 'X' or
                self.button1['text'] == 'X' and self.button4['text'] == 'X' and self.button7['text'] == 'X' or
                self.button2['text'] == 'X' and self.button5['text'] == 'X' and self.button8['text'] == 'X' or
                self.button3['text'] == 'X' and self.button6['text'] == 'X' and self.button9['text'] == 'X' or
                self.button1['text'] == 'X' and self.button5['text'] == 'X' and self.button9['text'] == 'X' or
                self.button7['text'] == 'X' and self.button5['text'] == 'X' and self.button3['text'] == 'X'):
            """Player 1 won"""
            self.victory(1)

        elif (self.button1['text'] == 'O' and self.button2['text'] == 'O' and self.button3['text'] == 'O' or
              self.button4['text'] == 'O' and self.button5['text'] == 'O' and self.button6['text'] == 'O' or
              self.button7['text'] == 'O' and self.button8['text'] == 'O' and self.button9['text'] == 'O' or
              self.button1['text'] == 'O' and self.button4['text'] == 'O' and self.button7['text'] == 'O' or
              self.button2['text'] == 'O' and self.button5['text'] == 'O' and self.button8['text'] == 'O' or
              self.button3['text'] == 'O' and self.button6['text'] == 'O' and self.button9['text'] == 'O' or
              self.button1['text'] == 'O' and self.button5['text'] == 'O' and self.button9['text'] == 'O' or
              self.button7['text'] == 'O' and self.button5['text'] == 'O' and self.button3['text'] == 'O'):
            """Player 2 won"""
            self.victory(2)

        elif (self.button1['state'] == 'disabled' and self.button2['state'] == 'disabled' and self.button3[
            'state'] == 'disabled' and
              self.button4['state'] == 'disabled' and self.button5['state'] == 'disabled' and self.button6[
                  'state'] == 'disabled' and
              self.button7['state'] == 'disabled' and self.button8['state'] == 'disabled' and self.button9[
                  'state'] == 'disabled'):
            self.victory(0)

    def start_game(self):
        self.main_frame.pack_forget()
        self.turn_label.pack()
        self.game_frame.pack(expand=1)

        self.button1.config(text='')
        self.button2.config(text='')
        self.button3.config(text='')
        self.button4.config(text='')
        self.button5.config(text='')
        self.button6.config(text='')
        self.button7.config(text='')
        self.button8.config(text='')
        self.button9.config(text='')
        self.button1.configure(state='normal')
        self.button2.configure(state='normal')
        self.button3.configure(state='normal')
        self.button4.configure(state='normal')
        self.button5.configure(state='normal')
        self.button6.configure(state='normal')
        self.button7.configure(state='normal')
        self.button8.configure(state='normal')
        self.button9.configure(state='normal')

        self.root.update()

        self.player1 = self.player1_entry.get()
        self.player2 = self.player2_entry.get()
        if str.lower(self.player2_entry.get()) == 'ai':
            print("Play against AI")
            self.player2 = 'AI'

        if len(self.player1) < 1:
            self.player1 = "Player 1"
        if len(self.player2) < 1:
            self.player2 = "Player 2"
        self.p1_turn = True
        turn_text = ("Its %s's turn!" % self.player1)
        self.turn_text.set(turn_text)

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=1)

        top_label_frame = tk.Label(self.main_frame, font='Times 16', textvariable=self.top_text)
        top_label_frame.grid(row=0, column=0, columnspan=3)

        player1_name = tk.Label(self.main_frame, font='Times 12', text='Player One:')
        player1_name.grid(row=1, column=0, padx=10)

        player2_name = tk.Label(self.main_frame, font='Times 12', text='Player Two:')
        player2_name.grid(row=2, column=0, padx=10)

        self.player1_entry = tk.Entry(self.main_frame, font='Times 12')
        self.player1_entry.grid(row=1, column=1, columnspan=2, padx=10)

        self.player2_entry = tk.Entry(self.main_frame, font='Times 12')
        self.player2_entry.grid(row=2, column=1, columnspan=2, padx=10)

        exit_button = tk.Button(self.main_frame, text='Exit', command=lambda: self.root.destroy())
        exit_button.grid(row=3, column=2, padx=10)

        play_button = tk.Button(self.main_frame, text='Play!', command=lambda: self.start_game())
        play_button.grid(row=3, column=1, pady=10, sticky='e')

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack_forget()

        self.turn_label = tk.Label(self.root, font='Times 30', textvariable=self.turn_text)
        self.turn_label.pack_forget()

        self.button1 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button1))
        self.button1.grid(row=3, column=0)
        self.button2 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button2))
        self.button2.grid(row=3, column=1)
        self.button3 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button3))
        self.button3.grid(row=3, column=2)
        self.button4 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button4))
        self.button4.grid(row=2, column=0)
        self.button5 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button5))
        self.button5.grid(row=2, column=1)
        self.button6 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button6))
        self.button6.grid(row=2, column=2)
        self.button7 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button7))
        self.button7.grid(row=1, column=0)
        self.button8 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button8))
        self.button8.grid(row=1, column=1)
        self.button9 = tk.Button(self.game_frame, height=1, width=4, text='', font='Times 26',
                                 command=lambda: self.on_click(self.button9))
        self.button9.grid(row=1, column=2)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tic Tac Toe')
        self.root.resizable(False, False)
        self.root.geometry("+550+400")
        self.main_frame = tk.Frame
        self.player1_entry = tk.Entry
        self.player2_entry = tk.Entry
        self.game_frame = tk.Frame
        self.turn_label = tk.Label
        self.button1 = tk.Button
        self.button2 = tk.Button
        self.button3 = tk.Button
        self.button4 = tk.Button
        self.button5 = tk.Button
        self.button6 = tk.Button
        self.button7 = tk.Button
        self.button8 = tk.Button
        self.button9 = tk.Button
        self.top_text = StringVar()
        self.turn_text = StringVar()
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.top_text.set('Welcome to Tic Tac Toe!\nPlease enter your player names.')
        self.p1_turn = True
        self.XO_list = []

        self.board = [' '] * 9

        print(self.board)
        self.create_widgets()
        self.root.mainloop()


if __name__ == '__main__':
    TicTacToe()
