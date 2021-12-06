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

# %%
print(test)
# %%
# TODO: split input up into parts - random numbers 
# and bingo cards
# TODO: figure out way to mark numbers and track numbers
# TODO: identify number of marked numbers in a row
