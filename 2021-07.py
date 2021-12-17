# Advent of code 2021 - Day 7!

# %%
# set up

import os
from aocd.models import Puzzle
import pandas as pd


import config as cf

# %%
# read in test data
with open('test.txt', 'r+') as my_file:
    test = my_file.read().split(',')

test = [int(x) for x in test]

# %%
# add environment variable for my unique submission
os.environ['AOC_SESSION'] = cf.SESSION_ID

# %%
# get puzzle
puzzle = Puzzle(year=2021, day=7)
# get data
sample = [int(x) for x in puzzle.input_data.split(',')]

# %%
print(test)
# %%
print(sample)

# %%
# part 1: most efficient hoizontal point
def main1(data):
    fuel_amounts = []
    for i in range(max(data)+1):
        fuel = sum([abs(x-i) for x in data])
        fuel_amounts.append(fuel)
    return min(fuel_amounts)

# %%
main1(test)
# %%
main1(sample)

# %%
# part 2:
def main2(data):
    fuel_amounts = []
    for i in range(max(data)+1):
        fuel = sum([((abs(x-i)*(abs(x-i)+1))/2) for x in data])  # equation for sum of natural numbers
        fuel_amounts.append(fuel)
    return min(fuel_amounts)

# %%
main2(test)
# %%
main2(sample)
# %%
