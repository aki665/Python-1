import random
import multiprocessing
import math
import time
import os
import tkinter as tk
from tkinter import simpledialog


def simulate(queue, batch_size, player_stay):
    deck = []

    def new_deck():
        std_deck = [
            # 2  3  4  5  6  7  8  9  10  J   Q   K   A
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, ]

        std_deck = std_deck * num_decks
        random.shuffle(std_deck)
        return std_deck[:]

    def play_hand():
        dealer_cards = []
        player_cards = []

        # deal initial cards
        player_cards.append(deck.pop(0))
        dealer_cards.append(deck.pop(0))
        player_cards.append(deck.pop(0))
        dealer_cards.append(deck.pop(0))


        #print(player_stay)
        #print(player_cards)
        while sum(player_cards) < player_stay:
            player_cards.append(deck.pop(0))
            #print(player_cards)

        # deal dealer on soft 17
        while sum(dealer_cards) < 18:
            exit = False
            # check for soft 17
            if sum(dealer_cards) == 17:
                exit = True
                # check for an ace and convert to 1 if found
                for i, card in enumerate(dealer_cards):
                    if card == 11:
                        exit = False
                        dealer_cards[i] = 1

            if exit:
                break

            dealer_cards.append(deck.pop(0))

        p_sum = sum(player_cards)
        d_sum = sum(dealer_cards)

        # dealer bust
        if d_sum > 21:
            return 1;
        # dealer tie
        if d_sum == p_sum:
            return 0;
        # dealer win
        if d_sum > p_sum:
            return -1;
        # dealer lose
        if d_sum < p_sum:
            return 1

    # starting deck
    deck = new_deck()

    # play hands
    win = 0
    draw = 0
    lose = 0
    for i in range(0, batch_size):
        # reshuffle cards at shuffle_perc percentage
        if (float(len(deck)) / (52 * num_decks)) * 100 < shuffle_perc:
            deck = new_deck()

        # play hand
        result = play_hand()

        # tally results
        if result == 1:
            win += 1
        if result == 0:
            draw += 1
        if result == -1:
            lose += 1

    # add everything to the final results
    queue.put([win, draw, lose])


num_decks = 4
shuffle_perc = 75
start_time = time.time()
simulations = 1000000
player_stay = 12

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    #simulations = tk.simpledialog.askinteger("Simulations", "How many BlackJack simulations do you want to run?",
                                           #  parent=root, minvalue=1)

    #player_stay = tk.simpledialog.askinteger("Simulations", "Where will the player stay?\n"
                                                          #  "(Simulation currently works only with 12)",
                                            # parent=root, minvalue=1, maxvalue=21)
    if simulations is None:
        simulations = 10000
    if player_stay is None:
        player_stay = 12

    #print(player_stay)
    # simulate
    cpus = multiprocessing.cpu_count() - 1
    batch_size = int(math.ceil(simulations / float(cpus)))

    queue = multiprocessing.Queue()

    # create n processes
    processes = []

    for i in range(0, cpus):
        process = multiprocessing.Process(target=simulate, args=(queue, batch_size, player_stay), daemon=True)
        processes.append(process)
        process.start()

    # wait for everything to finish
    for proc in processes:
        proc.join()

    finish_time = time.time() - start_time

    # get totals
    win = 0
    draw = 0
    lose = 0

    for i in range(0, cpus):
        results = queue.get()
        win += results[0]
        draw += results[1]
        lose += results[2]

    os.system('cls')
    print('  Cores used: %d' % cpus)
    print('  Total simulations: %d' % simulations)
    print('  Simulations/s: %d' % (float(simulations) / finish_time))
    print('  Execution time: %.2fs' % finish_time)
    print('  Player win percentage: %.2f%%' % ((win / float(simulations)) * 100))
    print('  Player draw percentage: %.2f%%' % ((draw / float(simulations)) * 100))
    print('  Player lose percentage: %.2f%%' % ((lose / float(simulations)) * 100))
    root.mainloop()
