import tkinter as tk
from tkinter import ttk, StringVar, simpledialog
from PIL import Image, ImageTk
import random
import glob
from time import sleep
import re
import asyncio
import threading
import concurrent.futures


class BlackJackWindow:

    def load(self):

        self.loading_frame = tk.Frame(self.root, bg='#FFFFFF')
        self.loading_frame.pack()

        label = tk.Label(self.loading_frame, font='Times 16', text='Please wait, while we load the game!', bg='#FFFFFF')
        label.pack()

        self.progressbar = ttk.Progressbar(self.loading_frame, length=52 * 4, mode='determinate', )
        self.progressbar["value"] = 0

        self.progressbar.pack()

        button = ttk.Button(self.loading_frame, text='Cancel', command=lambda: self.root.destroy(),
                            style="Cancel.TButton")
        button.pack(anchor='e')

        try:
            self.packs = int(simpledialog.askinteger("Input", "How many card decks do you want to use?\n(Default is 1)",
                                                     parent=self.root))
        except TypeError:
            # print("Failed to ask card pack size")
            self.packs = 1

        if self.packs <= 0:
            self.packs = 1

        self.progressbar["maximum"] = 52 * self.packs

        self.setup_images()
        self.create_widgets()

        self.loading_frame.pack_forget()
        self.root.geometry('1200x700+400+150')
        self.window_frame.pack()
        self.button_frame.pack(side='bottom', pady=15, fill='both')

    def setup_images(self):
        try:

            # self.card_list = []
            # self.filenames = []

            for filename in glob.glob('png_cards/*.png'):
                self.filenames.append(filename)
                im = Image.open(filename)
                im = im.resize((500 // 4, 726 // 4), Image.ANTIALIAS)
                im = ImageTk.PhotoImage(image=im)
                for i in range(self.packs):
                    self.card_list.append(im)

                    self.progressbar.step(1)
                    self.progressbar.update()

            for filename in glob.glob('png_card_back/*.png'):
                self.filenames.append(filename)
                im = Image.open(filename)
                im = im.resize((500 // 4, 726 // 4), Image.ANTIALIAS)
                self.card_back = ImageTk.PhotoImage(image=im)





        except:
            print("Error Loading Images")
            self.root.destroy()

        # #print(str(len(self.card_list)))

    def victory(self, who_wins, blackjack):
        self.games_played += 1
        if who_wins == 'Player' and blackjack == True:
            self.status_text.set("BLACKJACK!\nPlayer WINS!")
            self.player_wins_total += 1
            self.player_bj_total += 1

            self.deal_button.pack()
            self.deal_button['state'] = 'normal'
            self.stand_button.pack_forget()
            self.hit_button.pack_forget()



        elif who_wins == 'Player' and blackjack == False:
            self.status_text.set("Player WINS!")
            self.player_wins_total += 1

            self.deal_button.pack()
            self.deal_button['state'] = 'normal'
            self.stand_button.pack_forget()
            self.hit_button.pack_forget()

        elif who_wins == 'House' and blackjack == True:
            self.status_text.set("BLACKJACK!\nPlayer LOSES!")
            self.house_wins_total += 1
            self.house_bj_total += 1

            self.deal_button.pack()
            self.deal_button['state'] = 'normal'
            self.stand_button.pack_forget()
            self.hit_button.pack_forget()

        elif who_wins == 'House' and blackjack == False:
            self.status_text.set("Player LOSES!")
            self.house_wins_total += 1

            self.deal_button.pack()
            self.deal_button['state'] = 'normal'
            self.stand_button.pack_forget()
            self.hit_button.pack_forget()

        elif who_wins == 'Draw':
            self.status_text.set("It's a DRAW!")
            self.total_draws += 1

            self.deal_button.pack()
            self.deal_button['state'] = 'normal'
            self.stand_button.pack_forget()
            self.hit_button.pack_forget()
        self.update_total_games()

    def update_total_games(self):

        self.house_prosentile = round((self.house_wins_total / self.games_played) * 100, 2)
        self.player_prosentile = round((self.player_wins_total / self.games_played) * 100, 2)
        self.draw_prosentile = round((self.total_draws / self.games_played) * 100, 2)
        self.house_status_text.set(
            "House has won " + str(self.house_wins_total) + " games!\n " + str(self.house_prosentile) + "%"
            + "\nBlackjacks: " + str(self.house_bj_total))
        self.player_status_text.set(
            "Player has won " + str(self.player_wins_total) + " games!\n " + str(self.player_prosentile) + "%"
            + "\nBlackjacks: " + str(self.player_bj_total))
        self.draw_status_text.set(
            "Draws: " + str(self.total_draws) + "\n" + str(self.draw_prosentile) + "%")

    def check_card_value(self, who):

        if who == "Player":
            labels = self.player_labels

        elif who == "House":
            labels = self.house_labels

        aces = 0
        total_score = 0
        for text in labels:
            # print(text["image"][0])
            temp = text["image"][0].split("pyimage")
            name = self.filenames[int(temp[1]) - 1]
            temp = re.findall(r'\d+', name)
            score = int(temp[0])

            if score == 14:
                score = 11
                aces += 1

            elif score > 10:
                score = 10

            # print("Card value is ", score)

            total_score += score
        if who == 'Player':
            self.player_aces = aces
        elif who == 'House':
            self.house_aces = aces
        print("player aces ", self.player_aces)
        print("house aces ", self.house_aces)
        return total_score

    def deal_a_card(self, to_who):
        if to_who == 'House':
            image = (random.choice(self.card_list))
            self.house_card = ttk.Label(self.dealer_frame, image=image)
            self.house_card.pack(side='left')
            self.root.update()
            self.house_labels.append(self.house_card)
        elif to_who == 'Player':
            image = (random.choice(self.card_list))
            self.player_card = ttk.Label(self.player_frame, image=image)
            self.player_card.pack(side='left')
            self.root.update()
            self.player_labels.append(self.player_card)

        self.player_total = self.check_card_value('Player')
        self.house_total = self.check_card_value('House')
        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))

    def deal(self):
        """
        Deals 2 cards to House and Player. First (House's) card is not revealed
        Button will vanish after pressing and reappear when round is over
        :return: None
        """
        self.deal_button.pack_forget()
        self.hit_button['state'] = 'disabled'
        self.stand_button['state'] = 'disabled'
        self.hit_button.pack(side='left', anchor='center', padx=50)
        self.stand_button.pack(side='right', anchor='center', padx=50)
        self.house_aces = 0
        self.player_aces = 0
        self.player_total = 0
        self.house_total = 0
        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))
        self.status_text.set("Dealing cards")

        for label in self.house_labels:
            label.destroy()

        for label in self.player_labels:
            label.destroy()

        self.house_labels = []
        self.player_labels = []

        self.root.update()
        for x in range(2):
            if x == 0:
                image = self.card_back
                self.house_card = ttk.Label(self.dealer_frame, image=image)
                self.house_card.pack(side='left')
                self.root.update()
                self.house_labels.append(self.house_card)
                self.back_card = True
                sleep(0.5)
            else:
                self.deal_a_card('House')
                sleep(0.5)

            self.deal_a_card('Player')
            sleep(0.5)

        self.player_total = self.check_card_value('Player')
        self.house_total = self.check_card_value('House')
        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))

        if self.player_total == 21:
            self.victory('Player', True)
        else:
            self.hit_button['state'] = 'normal'
            self.stand_button['state'] = 'normal'
            self.status_text.set("Let's play!")

    def hit(self, house_or_player):
        """
        Deals player 1 card from card_list and checks if player has less than 21 after dealing
        If house_or_player == house, then will deal cards to house. House has to hit 17 or lover and stand if 18 or more
        """
        # print('Deal to %s' % house_or_player)
        self.hit_button['state'] = 'disabled'
        self.stand_button['state'] = 'disabled'
        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))

        if house_or_player == 'Player':
            self.player_total = self.check_card_value('Player')
            self.deal_a_card('Player')
            self.player_total = self.check_card_value('Player')
            # print(self.player_total)

            if self.player_total > 21:
                while self.player_total > 21 and self.player_aces > 0:
                    # print("Players ACE's: ", self.player_aces)
                    self.player_total -= 10
                    self.player_aces -= 1
                    self.house_total_text.set(str(self.house_total))
                    self.player_total_text.set(str(self.player_total))
                if self.player_total > 21:
                    # print("YOU LOST")

                    self.victory('House', False)

            if self.player_total == 21:
                self.hit_button['state'] = 'disabled'
                self.player_total_text.set(str(self.player_total))
                self.root.update()
                sleep(1)
                self.hit("House")

        if house_or_player == 'House':
            self.hit_button['state'] = 'disabled'
            self.stand_button['state'] = 'disabled'

            """Remove the back side card"""
            if self.back_card:
                self.house_labels[0].config(image=random.choice(self.card_list))
                self.back_card = False
                self.house_total = self.check_card_value("House")
                self.house_total_text.set(str(self.house_total))
                self.root.update()


            if self.house_total == 21:
                self.victory('House', True)
            else:
                while self.house_total < 17:

                    sleep(1.5)
                    self.deal_a_card("House")
                    self.house_total = self.check_card_value("House")
                    self.house_total_text.set(str(self.house_total))
                    self.root.update()

                    if self.house_total > 21:

                        while self.house_total > 21 and self.house_aces > 0:
                            self.house_total -= 10
                            self.house_total_text.set(str(self.house_total))
                            self.house_aces -= 1

                        self.house_total_text.set(str(self.house_total))

                if self.house_total > 21 and self.house_aces == 0:
                    # print("House Loses")
                    self.victory('Player', False)


                elif self.house_total == 21 and self.player_total < 21:
                    # print("Player Loses")
                    self.victory('House', False)

                elif self.house_total == self.player_total:
                    # print("Draw")
                    self.victory('Draw', False)


                elif self.house_total >= 17 and self.player_total < self.house_total:
                    # print("Player Loses")
                    self.victory('House', False)



                elif self.house_total >= 17 and self.player_total > self.house_total:
                    # print("Player Wins")
                    self.victory('Player', False)

        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))
        self.hit_button['state'] = 'normal'
        self.stand_button['state'] = 'normal'

    def create_widgets(self):
        self.window_frame = ttk.Frame(self.root)

        self.dealer_frame = ttk.Frame(self.window_frame, height=(500 // 4), width=(726 // 4))
        self.dealer_frame.grid(row=0, column=1, pady=30, padx=50)
        for x in range(2):
            self.deal_a_card('House')

        house_label = ttk.Label(self.window_frame, textvariable=self.house_total_text, )
        house_label.grid(row=0, column=0)

        self.player_frame = ttk.Frame(self.window_frame, height=(500 // 4), width=(726 // 4))
        self.player_frame.grid(row=2, column=1, pady=30, padx=50)
        for x in range(2):
            self.deal_a_card('Player')

        player_label = ttk.Label(self.window_frame, textvariable=self.player_total_text)
        player_label.grid(row=2, column=0)

        self.status_frame = ttk.Frame(self.window_frame)
        self.status_frame.grid(row=1, column=1)

        status_label = ttk.Label(self.status_frame, textvariable=self.status_text)
        status_label.pack(anchor='center', )

        self.button_frame = ttk.Frame(self.root)

        self.deal_button = ttk.Button(self.button_frame, text='Deal', style="Deal.TButton", command=lambda: self.deal())

        self.deal_button.pack()

        self.stand_button = ttk.Button(self.button_frame, text='Stand', style="Stand.TButton",
                                       command=lambda: self.hit('House'))

        self.hit_button = ttk.Button(self.button_frame, text='Hit', style="Hit.TButton",
                                     command=lambda: self.hit('Player'))

        self.result_frame = ttk.Frame(self.window_frame, )
        self.result_frame.grid(row=0, column=2, pady=30, padx=50)

        dealer_status = tk.Label(self.window_frame, textvariable=self.house_status_text, background="#00650F",
                                 font='Times 20')
        dealer_status.grid(row=0, column=2)

        player_status = tk.Label(self.window_frame, textvariable=self.player_status_text, background="#00650F",
                                 font='Times 20')
        player_status.grid(row=2, column=2)

        draw_status = tk.Label(self.window_frame, textvariable=self.draw_status_text, background="#00650F",
                               font='Times 20')
        draw_status.grid(row=1, column=2)

    def __init__(self):
        self.root = tk.Tk()

        # #print(self.root.winfo_class())

        self.root.title('BlackJack')
        self.root.geometry('+750+450')
        self.root.config(bg='#00650F')
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)

        ttk.Style().configure(".", background="#00650F", font='Times 40')
        ttk.Style().configure("Deal.TButton", backgorund='#064200', foreground='#064200', activeforeground='#00650F',
                              font='Times 32', )
        ttk.Style().configure("Hit.TButton", background='#D42D1A', foreground='#D42D1A', font='Times 32')
        ttk.Style().configure("Stand.TButton", background='#4107A7', foreground='#4107A7', font='Times 32')
        ttk.Style().configure("Cancel.TButton", background='White', font='Times 12')

        self.packs = None
        self.player_total = 0
        self.player_aces = 0
        self.house_total = 0
        self.house_aces = 0

        self.games_played = 0
        self.player_wins_total = 0
        self.house_wins_total = 0
        self.total_draws = 0
        self.player_bj_total = 0
        self.house_bj_total = 0

        # self.house_prosentile = round((self.house_wins_total / self.games_played)*100, 2)
        # self.player_prosentile = round((self.player_wins_total / self.games_played)*100, 2)
        self.house_prosentile = 0
        self.player_prosentile = 0
        # self.draw_prosentile = round((self.total_draws / self.games_played)*100, 2)
        self.draw_prosentile = 0

        self.back_card = True
        self.dealing = False

        self.house_total_text = StringVar()
        self.player_total_text = StringVar()
        self.draw_status_text = StringVar()
        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))
        self.draw_status_text.set(str(self.total_draws))

        self.status_text = StringVar()
        self.status_text.set("")

        self.house_status_text = StringVar()
        self.player_status_text = StringVar()
        self.house_status_text.set(
            "House has won " + str(self.house_wins_total) + " games!\n " + str(self.house_prosentile) + "%"
            + "\nBlackjakcs: " + str(self.house_bj_total))
        self.player_status_text.set(
            "Player has won " + str(self.player_wins_total) + " games!\n " + str(self.player_prosentile) + "%"
            + "\nBlackjakcs: " + str(self.house_bj_total))
        self.draw_status_text.set(
            "Draws: " + str(self.total_draws) + "\n" + str(self.draw_prosentile) + "%")

        self.card_list = []
        self.filenames = []
        self.house_labels = []
        self.player_labels = []
        self.button_names = []
        self.button_img = []

        self.loading_frame = ttk.Frame
        self.progressbar = ttk.Progressbar
        self.window_frame = ttk.Frame
        self.dealer_frame = ttk.Frame
        self.house_card = ttk.Label
        self.player_card = ttk.Label
        self.player_frame = ttk.Frame

        self.button_frame = ttk.Frame
        self.start_button = ttk.Button
        self.stand_button = ttk.Button
        self.hit_button = ttk.Button
        self.deal_button = ttk.Button

        self.load()

        self.root.mainloop()


if __name__ == '__main__':
    BlackJackWindow()
