# Advent of code 2021 - Day 5!

# %%
# set up

import os
from aocd.models import Puzzle
import pandas as pd
import re

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
puzzle = Puzzle(year=2021, day=5)
# get data
sample = puzzle.input_data.splitlines()

# %%
print(test)
# %%
print(sample)

# %%
# part 1

# regex to identify different values
coordRegex = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

def main1(data):
    x_max = y_max = 0

    # create grid
    for value in data:
        co = coordRegex.search(value)
        x1 = int(co.group(1))
        y1 = int(co.group(2))
        x2 = int(co.group(3))
        y2 = int(co.group(4))

        if x1 == x2 or y1 == y2:
            x_max = max(x_max, x1, x2)
            y_max = max(y_max, y1, y2)
        else:
            continue

    grid = [[0] * (x_max+1) for _ in range(y_max+1)]  

    # update grid with vent counts
    for value in data:
        co = coordRegex.search(value)
        x1 = int(co.group(1))
        y1 = int(co.group(2))
        x2 = int(co.group(3))
        y2 = int(co.group(4))

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x] += 1
        else:
            continue

    points = sum(val > 1 for row in grid for val in row)

    return points

# %%
main1(test)

main1(sample)

# %%
# part 2
def main2(data):
    x_max = y_max = 0

    # create grid
    for value in data:
        co = coordRegex.search(value)
        x1 = int(co.group(1))
        y1 = int(co.group(2))
        x2 = int(co.group(3))
        y2 = int(co.group(4))

        x_max = max(x_max, x1, x2)
        y_max = max(y_max, y1, y2)
        
    grid = [[0] * (x_max+1) for _ in range(y_max+1)]  

    # update grid with vent counts
    for value in data:
        co = coordRegex.search(value)
        x1 = int(co.group(1))
        y1 = int(co.group(2))
        x2 = int(co.group(3))
        y2 = int(co.group(4))

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[y][x] += 1
        else:
            if x1 < x2:
                x = [*range(x1, x2+1)]
            else:
                x = [*range(x1, x2-1, -1)]
            if y1 < y2:
                y = [*range(y1, y2+1)]
            else:
                y = [*range(y1, y2-1, -1)]
            
            for i in range(len(x)):
                grid[y[i]][x[i]] += 1

    points = sum(val > 1 for row in grid for val in row)

    return points

# %%
main2(test)

main2(sample)

# %%
