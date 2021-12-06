# Advent of code 2021 - Day 3!

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
puzzle = Puzzle(year=2021, day=3)
# get data
sample = puzzle.input_data.splitlines()

# %%
# Part 1:
def part1(data):
    # get lists of digits in each position
    digits = []
    for d in range(len(data[0])):
        ds = [x[d] for x in data]
        digits.append(ds)

    # sum up amounts in each position
    totals = []
    for item in digits:
        item = [int(x) for x in item]
        totals.append(sum(item))

    # if amount is more than half length of diagnostics, then
    # gamma = 1, epsilon = 0. Otherwise this is reversed.
    gamma = []
    epsilon = []
    for total in totals:
        if total >= len(data)/2:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')

    # convert str version of binary to decimal (base 2 for binary)
    gamma_dec = int(''.join(gamma), 2)
    epsilon_dec = int(''.join(epsilon), 2)

    print('Gamma decimal:', gamma_dec, 'Epsilon decimal:', epsilon_dec)
    print('Power consumption is:', gamma_dec*epsilon_dec)

# %%
part1(test)
part1(sample)


# %%
# Part 2:

def part2(data):

    oxygen_data = data
    co2scrubber_data = data

    # oxygen generator rating
    for d in range(len(oxygen_data[0])):
        if len(oxygen_data) == 1:
            break
        bits = [x[d] for x in oxygen_data]

        # summarise bits to find most common
        zeros = bits.count('0')
        ones = bits.count('1')

    # keep entries with most frequent values in bit position
        if ones >= zeros:
            oxygen_data = [x for x in oxygen_data if x[d] == '1']
        else:
            oxygen_data = [x for x in oxygen_data if x[d] == '0']

    oxygen = int(oxygen_data[0], 2)   

    print('Oxygen generator rating:', oxygen) 


    # CO2 scrubber rating
    for d in range(len(co2scrubber_data[0])):
        if len(co2scrubber_data) == 1:
            break
        bits = [x[d] for x in co2scrubber_data]

        # summarise bits to find most common
        zeros = bits.count('0')
        ones = bits.count('1')

        # keep entries with least frequent values in bit position
        if zeros <= ones:
            co2scrubber_data = [x for x in co2scrubber_data if x[d] == '0']
        else:
            co2scrubber_data = [x for x in co2scrubber_data if x[d] == '1']

    co2scrubber = int(co2scrubber_data[0], 2)   

    print('Co2 scrubber rating:', co2scrubber) 
    print('Life support rating:', oxygen*co2scrubber)
    print('\n')

# %%
part2(test)
# %%
part2(sample)
# %%
