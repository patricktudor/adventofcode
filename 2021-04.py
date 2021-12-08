# Advent of code 2021 - Day 4!

# %%
# set up

import os
from aocd.models import Puzzle
import pandas as pd

import config as cf

# %%
# read in test data
with open('test.txt', 'r+') as my_file:
    test = my_file.read().splitlines()

# %%
# add environment variable for my unique submission
os.environ['AOC_SESSION'] = cf.SESSION_ID

# %%
# get puzzle
puzzle = Puzzle(year=2021, day=4)
# get data
sample = puzzle.input_data.splitlines()

# split input up into parts - random numbers and bingo cards
# %%
# get indexes of '' items in list
def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

# %% 
# Part 1:
def main1(data):
    splits = get_index_positions(data, '')
    #Perform the split
    split_data = [data[i: j] for i, j in zip([0] + splits, splits + [None])]
    # remove instances of ''
    parts = []
    for lst in split_data:
        lst = [value for value in lst if value != '']
        parts.append(lst)
    nums = parts[0]
    num_lst = [x.split(',') for x in nums]
    num_lst = [i for sublst in num_lst for i in sublst]  # flatten nested list
    
    # bingo cards
    bingo_cards = []
    for bingo in parts[1:]:
        card = []
        for line in bingo:
            line = [int(x) for x in line.split()]
            card.append(line)
        bingo_cards.append(card)

    # mark cards with x
    try:
        for n, num in enumerate(num_lst):
            for c, card in enumerate(bingo_cards):
                for i in range(5):
                    for j in range(5):
                        if card[i][j] == int(num):
                            bingo_cards[c][i][j] = 'x'

            # count number of x in each row and column
            for c, card in enumerate(bingo_cards):
                for i in range(5):
                    if card[i].count('x') == 5:
                        print(f'Count of row {i} of card {c} for #{n}:', card[i].count('x'))
                        raise StopIteration
                for j in range(5):
                    column = [card[i][j] for i in range(5)]
                    if column.count('x') == 5:
                        print(f'Count of column {j} of card {c} for #{n}:', column.count('x'))
                        raise StopIteration
    except StopIteration:
        pass

    # sum up values not read out
    winning_card = [x for line in card for x in line if x != 'x']
    score = sum(winning_card)

    print('Final score is:', int(num)*score)
    print('\n')

# %%
main1(test)
main1(sample)

# %%
# Part 2:
def main2(data):
    splits = get_index_positions(data, '')
    #Perform the split
    split_data = [data[i: j] for i, j in zip([0] + splits, splits + [None])]
    # remove instances of ''
    parts = []
    for lst in split_data:
        lst = [value for value in lst if value != '']
        parts.append(lst)
    nums = parts[0]
    num_lst = [x.split(',') for x in nums]
    num_lst = [i for sublst in num_lst for i in sublst]  # flatten nested list
    
    # bingo cards
    bingo_cards = []
    for bingo in parts[1:]:
        card = []
        for line in bingo:
            line = [int(x) for x in line.split()]
            card.append(line)
        bingo_cards.append(card)

    # card turns for bingo dictionary
    d = {}
    for c, card in enumerate(bingo_cards):
        try:
            for n, num in enumerate(num_lst):
                for i in range(5):
                    for j in range(5):
                        if card[i][j] == int(num):
                            bingo_cards[c][i][j] = 'x'
                for i in range(5):
                    if card[i].count('x') == 5:
                        # print(f'Count of row {i} of card {c} for #{n}:', card[i].count('x'))
                        raise StopIteration
                for j in range(5):
                    column = [card[i][j] for i in range(5)]
                    if column.count('x') == 5:
                        # print(f'Count of column {j} of card {c} for #{n}:', column.count('x'))
                        raise StopIteration
        except StopIteration:
            pass
        # print(f'Card {c}, Number:', num, 'Index:', n)
        d[c] = n
 
    mk = max(d, key=d.get)  # key with max turns

    losing_card = bingo_cards[mk]
    # sum up values not read out
    losing_card = [x for line in losing_card for x in line if x != 'x']
    score = sum(losing_card)
    
    # find last used num for last bingo card
    last_num = num_lst[d.get(mk)]

    print('Final score is:', int(last_num)*score)
    print('\n')

# %%
main2(test)
main2(sample)
# %%
