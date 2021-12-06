# Advent of code 2021 - Day 2!

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
puzzle = Puzzle(year=2021, day=2)
# get data
move = puzzle.input_data.splitlines()
# split string at whitespace
move = [str.split(x) for x in move]
# change number strings to integers
move = [[x, int(y)] for x, y in move]

# %%
# Part 1: what is the multiple of total horizontal and 
# depth amounts?

horizontal = depth = 0

for x, y in move:
    if x == 'forward':
        horizontal += y
    elif x == 'down':
        depth += y
    elif x == 'up':
        depth -= y

print("Horizontal is:", horizontal, "Depth is:", depth)

print('Value to submit is:', horizontal*depth)

# %%
# Part 2: what is the multiple of total horizontal and depth amounts?
# Note: down X increases aim by X
#       up X decreases aim by X
#       forward X increases horizontal by X
#       also increases depth by aim multiplied by X

horizontal = depth = aim = 0

for x, y in move:
    if x == 'down':
        aim += y
    elif x == 'up':
        aim -= y
    elif x == 'forward':
        horizontal += y
        depth += aim*y

print("Horizontal is:", horizontal, "Depth is:", depth)

print('Value to submit is:', horizontal*depth)

# %%
