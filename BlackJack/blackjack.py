import tkinter as tk
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
import random
import glob
from time import sleep
import re


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

    def check_card_value(self, who):

        if who == "Player":
            labels = self.player_labels

        elif who == "House":
            labels = self.house_labels

        total_score = 0
        for text in labels:
            temp = text["image"].split("pyimage")
            name = self.filenames[int(temp[1]) - 1]
            temp = re.findall(r'\d+', name)
            score = int(temp[0])

            if score == 14 and who == 'Player':
                score = 11
                self.player_aces += 1
            elif score == 14 and who == 'House':
                score = 11
                self.house_aces += 1

            elif score > 10:
                score = 10

            print("Card value is ", score)

            total_score += score

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
        # self.deal_button.pack_forget()
        self.hit_button['state'] = 'normal'
        self.stand_button['state'] = 'normal'
        self.hit_button.pack(side='left', anchor='center', padx=50)
        self.stand_button.pack(side='right', anchor='center', padx=50)
        self.player_total = 0

        for label in self.house_labels:
            # print(label["image"])
            label.config(image="")

        for label in self.player_labels:
            label.config(image="")

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
        print(self.player_total)

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
                if self.player_aces > 0:
                    self.player_total -= 10
                    self.player_aces -= 1
                else:
                    print("YOU LOST")
                    self.hit_button['state'] = 'disabled'
                    self.stand_button['state'] = 'disabled'
                    print("Player Total is          ", self.player_total)
            elif self.player_total == 21:
                self.hit_button['state'] = 'disabled'
                self.hit("House")

        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))

        if house_or_player == 'House':
            pass

    def create_widgets(self):
        self.window_frame = tk.Frame(self.root)
        self.window_frame.pack_forget()

        self.dealer_frame = tk.Frame(self.window_frame, height=(500 // 4), width=(726 // 4))
        self.dealer_frame.grid(row=0, column=1, pady=30, padx=50)
        for x in range(2):
            self.deal_a_card('House')


        house_label = tk.Label(self.window_frame, textvariable=self.house_total_text, font='Times 25')
        house_label.grid(row=0, column=0, padx=10)

        self.player_frame = tk.Frame(self.window_frame, height=(500 // 4), width=(726 // 4))
        self.player_frame.grid(row=1, column=1, pady=30, padx=50)
        for x in range(2):
            self.deal_a_card('Player')

        player_label = tk.Label(self.window_frame, textvariable=self.player_total_text, font='Times 25')
        player_label.grid(row=1, column=0, padx=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack_forget()

        self.deal_button = tk.Button(self.button_frame, text='Deal', command=lambda: self.deal())
        self.deal_button.pack()

        self.stand_button = tk.Button(self.button_frame, text='Stand', command=lambda: self.hit('House'))
        self.stand_button.pack_forget()

        self.hit_button = tk.Button(self.button_frame, text='Hit', command=lambda: self.hit('Player'))
        self.hit_button.pack_forget()

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('BlackJack')
        self.root.geometry('+450+350')

        self.packs = 1
        self.player_total = 0
        self.player_aces = 0
        self.house_total = 0
        self.house_aces = 0

        self.house_total_text = StringVar()
        self.player_total_text = StringVar()
        self.house_total_text.set(str(self.house_total))
        self.player_total_text.set(str(self.player_total))


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

        self.root.mainloop()


if __name__ == '__main__':
    BlackJackWindow()
