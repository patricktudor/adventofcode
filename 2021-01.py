# Advent of code 2021 - Day 1!

# %%
# set up

import os
from aocd.models import Puzzle
import pandas as pd

import config as cf

# %%
# add environment variable for my unique submission
os.environ['AOC_SESSION'] = cf.SESSION_ID

# %%
# get puzzle
puzzle = Puzzle(year=2021, day=1)
# get data
depths = puzzle.input_data.splitlines()
# convert strings to integers
depths = [int(x) for x in depths]

# %%
# Part 1: how many times does the depth increase?

counter = 0

for i, depth in enumerate(depths):
    if i == 0:
        continue
    if depth > depths[i-1]:
        counter += 1
    else:
        continue

print('The depth increases', counter, 'times.')

# %%
# Part 2: How many times does the sum of measurements
# in a three value sliding window increase?

counter = 0

for i, depth in enumerate(depths):
    if i <= 2:
        continue
    currentsum = depth + depths[i-1] + depths[i-2]
    previoussum = depths[i-1] + depths[i-2] + depths[i-3]
    print(i, currentsum, previoussum, counter)
    if currentsum > previoussum:
        counter += 1
    else:
        continue

print('The 3-value depth increases', counter, 'times.')
# %%
