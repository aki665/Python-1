import tkinter as tk
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
import random
import glob
from time import sleep
import re
import asyncio


class BlackJackWindow:

    def load(self):

        self.loading_frame = tk.Frame(self.root)
        self.loading_frame.pack()

        label = tk.Label(self.loading_frame, font='Times 16', text='Please wait while we load the game!')
        label.pack()

        self.progressbar = ttk.Progressbar(self.loading_frame, length=52 * 4, mode='determinate')
        self.progressbar["value"] = 0
        self.progressbar["maximum"] = 52 * self.packs
        self.progressbar.pack(side='bottom')

        self.setup_images()
        self.create_widgets()

        self.loading_frame.pack_forget()
        self.window_frame.pack()
        self.button_frame.pack(side='bottom', pady=15, fill='both')

    def setup_images(self):
        try:

            # self.card_list = []
            # self.filenames = []
            for i in range(self.packs):
                for filename in glob.glob('png_cards/*.png'):
                    self.filenames.append(filename)
                    im = Image.open(filename)
                    im = im.resize((500 // 4, 726 // 4), Image.ANTIALIAS)
                    im = ImageTk.PhotoImage(image=im)
                    self.card_list.append(im)

                    self.progressbar.step(1)
                    self.progressbar.update()

            for filename in glob.glob('png_card_back/*.png'):
                self.filenames.append(filename)
                im = Image.open(filename)
                im = im.resize((500 // 4, 726 // 4), Image.ANTIALIAS)
                self.card_back = ImageTk.PhotoImage(image=im)




        except:
            self.root.destroy()

        # print(str(len(self.card_list)))

    async def update_label_text(self):
        try:
            while True:
                self.house_total_text.set(str(self.house_total))
                self.player_total_text.set(str(self.player_total))

                self.root.update()
        except tk.TclError:
            print("TclError")

    def victory(self, who_wins, blackjack):
        if who_wins == 'Player' and blackjack == True:
            self.status_text.set("BLACKJACK!!!\nPlayer WINS!")
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

        elif who_wins == 'House' and blackjack ==True:
            self.status_text.set("BLACKJACK!!!\nPlayer LOSES!")
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

    def check_card_value(self, who):

        if who == "Player":
            labels = self.player_labels

        elif who == "House":
            labels = self.house_labels

        aces = 0
        total_score = 0
        for text in labels:
            temp = text["image"].split("pyimage")
            name = self.filenames[int(temp[1]) - 1]
            temp = re.findall(r'\d+', name)
            score = int(temp[0])


            if score == 14:
                score = 11
                aces += 1

            elif score > 10:
                score = 10

            print("Card value is ", score)

            total_score += score
        if who == 'Player':
            self.player_aces = aces
        elif who == 'House':
            self.house_aces = aces



        return total_score

    def deal_a_card(self, to_who):
        if to_who == 'House':
            image = (random.choice(self.card_list))
            self.house_card = tk.Label(self.dealer_frame, image=image)
            self.house_card.pack(side='left')
            self.root.update()
            self.house_labels.append(self.house_card)
        elif to_who == 'Player':
            image = (random.choice(self.card_list))
            self.player_card = tk.Label(self.player_frame, image=image)
            self.player_card.pack(side='left')
            self.root.update()
            self.player_labels.append(self.player_card)



    def deal(self):
        """
        Deals 2 cards to House and Player. First (House's) card is not revealed
        Button will vanish after pressing and reappear when round is over
        :return: None
        """
        self.deal_button.pack_forget()
        self.hit_button['state'] = 'normal'
        self.stand_button['state'] = 'normal'
        self.hit_button.pack(side='left', anchor='center', padx=50)
        self.stand_button.pack(side='right', anchor='center', padx=50)
        self.house_aces = 0
        self.player_aces = 0
        self.player_total = 0
        self.house_total = 0
        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))
        self.status_text.set("Dealing")



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
                self.house_card = tk.Label(self.dealer_frame, image=image)
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
        #self.house_total_text.set(str(self.house_total))
        #self.player_total_text.set(str(self.player_total))
        print(self.player_total)

        if self.player_total == 21:
            self.victory('Player', True)

        self.status_text.set("Let's play!")

    def hit(self, house_or_player):
        """
        Deals player 1 card from card_list and checks if player has less than 21 after dealing
        If house_or_player == house, then will deal cards to house. House has to hit 16 or lover and stand if 17 or more
        """
        print('Deal to %s' % house_or_player)

        if house_or_player == 'Player':
            self.player_total = self.check_card_value('Player')
            self.deal_a_card('Player')
            self.player_total = self.check_card_value('Player')
            print(self.player_total)

            if self.player_total > 21:
                while self.player_total > 21 and self.player_aces > 0:
                        print("Players ACE's: ", self.player_aces)
                        self.player_total -= 10
                        self.player_aces -= 1
                if self.player_total > 21:
                    print("YOU LOST")

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
            if self.back_card == True:

                self.house_labels[0].config(image=random.choice(self.card_list))

                self.back_card = False
                self.house_total = self.check_card_value("House")




            while self.house_total < 18:
                sleep(1.5)
                self.deal_a_card("House")
                self.house_total = self.check_card_value("House")
                self.house_total_text.set(str(self.house_total))
                self.root.update()

                if self.house_total > 21:


                    while self.house_total > 21 and self.house_aces > 0:
                            self.house_total -= 10
                            self.house_aces -= 1


                    if self.house_total > 21:
                        print("Player wins")
                        self.victory('Player', False)
                        break








            if self.house_total > 21:
                print("House Loses")
                self.victory('Player', False)


            elif self.house_total == 21 and self.player_total < 21:
                print("Player Loses")
                self.victory('House', False)

            elif self.house_total == self.player_total:
                print("Draw")
                self.victory('Draw', False)
                self.status_text.set("It's a draw")

            elif self.house_total >= 18 and self.player_total < self.house_total:
                print("Player Loses")
                self.victory('House', False)

                self.deal_button['state'] = 'normal'

            elif self.house_total >= 18 and self.player_total > self.house_total:
                print("Player Wins")
                self.victory('Player', False)


        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))


    def create_widgets(self):
        self.window_frame = tk.Frame(self.root)
        self.window_frame.pack_forget()

        self.dealer_frame = tk.Frame(self.window_frame, height=(500 // 4), width=(726 // 4))
        self.dealer_frame.grid(row=0, column=1, pady=30, padx=50)
        for x in range(2):
            self.deal_a_card('House')

        house_label = tk.Label(self.window_frame, textvariable=self.house_total_text, font='Times 25')
        house_label.grid(row=0, column=0)

        self.player_frame = tk.Frame(self.window_frame, height=(500 // 4), width=(726 // 4))
        self.player_frame.grid(row=2, column=1, pady=30, padx=50)
        for x in range(2):
            self.deal_a_card('Player')

        player_label = tk.Label(self.window_frame, textvariable=self.player_total_text, font='Times 25')
        player_label.grid(row=2, column=0)

        self.status_frame = tk.Frame(self.window_frame)
        self.status_frame.grid(row=1, column=1)

        status_label = tk.Label(self.status_frame, textvariable=self.status_text, font='Times 25')
        status_label.pack(anchor='center', )

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack_forget()

        self.deal_button = tk.Button(self.button_frame, text='Deal', command=lambda: self.deal(), font='Times 20')
        self.deal_button.pack()

        self.stand_button = tk.Button(self.button_frame, text='Stand', command=lambda: self.hit('House'), font='Times 20')
        self.stand_button.pack_forget()

        self.hit_button = tk.Button(self.button_frame, text='Hit', command=lambda: self.hit('Player'), font='Times 20')
        self.hit_button.pack_forget()

    def __init__(self):
        self.root = tk.Tk()

        #print(self.root.winfo_class())



        self.root.title('BlackJack')
        self.root.geometry('+450+350')


        self.packs = 1
        self.player_total = 0
        self.player_aces = 0
        self.house_total = 0
        self.house_aces = 0

        self.player_wins_total = 0
        self.house_wins_total = 0
        self.total_draws = 0
        self.player_bj_total = 0
        self.house_bj_total = 0

        self.back_card = True

        self.house_total_text = StringVar()
        self.player_total_text = StringVar()
        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))

        self.status_text = StringVar()
        self.status_text.set("")

        self.card_list = []
        self.filenames = []
        self.house_labels = []
        self.player_labels = []

        self.loading_frame = tk.Frame
        self.progressbar = ttk.Progressbar
        self.window_frame = tk.Frame
        self.dealer_frame = tk.Frame
        self.house_card = tk.Label
        self.player_card = tk.Label
        self.player_frame = tk.Frame

        self.button_frame = tk.Frame
        self.start_button = tk.Button
        self.stand_button = tk.Button
        self.hit_button = tk.Button
        self.deal_button = tk.Button

        self.load()

        try:
            asyncio.run(self.update_label_text())
        except ValueError:
            print("Async Error")
        self.root.mainloop()


if __name__ == '__main__':



    BlackJackWindow()
