# Advent of code 2021 - Day 6!

# %%
# set up

import os
from aocd.models import Puzzle
from collections import Counter
import pandas as pd

import config as cf

# %%
# read in test data
with open('test.txt', 'r+') as my_file:
    test = my_file.read().split(',')

# %%
# add environment variable for my unique submission
os.environ['AOC_SESSION'] = cf.SESSION_ID

# %%
# get puzzle
puzzle = Puzzle(year=2021, day=6)
# get data
sample = puzzle.input_data.split(',')

# %%
print(test)
# %%
print(sample)

# %%
# part 1
def main1(data, days):
    for day in range(1, days+1):
        new = 0
        vals = []
        for val in data:
            if val == '0':
                val = '6'
                new += 1
            else:
                val = int(val)
                val += -1
                val = str(val)
            vals.append(val)
        data = vals
        
        if new > 0:
            data.extend(['8' for i in range(new)])

    return len(data)

# %%
main1(test, 80)
# %%
main1(sample, 80)


# %%
# part 2: need a more elegant way to do the same as part 1
def main2(data, days):
    # initial dataset
    val_dict = Counter(data)
    valdf = pd.DataFrame.from_dict(val_dict, orient="index").reset_index()
    valdf = valdf.rename(columns={"index": "Current_Timer", 0: "Amount"})

    # set up template table to update
    updatedf = pd.DataFrame(
        {
            "Current_Timer": ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
            "Next_Timer": ['6','0', '1', '2', '3', '4', '5', '6', '7'],
        },
        index=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    )

    # join to initial values
    df = pd.merge(updatedf[["Current_Timer", "Next_Timer"]], 
                    valdf[["Current_Timer", "Amount"]], 
                    on="Current_Timer", 
                    how="left").fillna(0)
    
    # loop through days
    for day in range(days):
        df_copy = df.copy()
        new = df.at[0, "Amount"]  # get number of new lanternfish
    
        # join df to itself
        new_df = pd.merge(df[["Current_Timer", "Next_Timer"]], 
                            df_copy[["Next_Timer", "Amount"]], 
                            left_on="Current_Timer",
                            right_on="Next_Timer", 
                            how="left",
                            suffixes=(None, "_toremove"))

        # fill in new lanternfish
        new_df.at[9, "Amount"] = new

        # group to remove duplicated rows, sum amounts and reset index
        df = new_df.groupby(["Current_Timer", "Next_Timer"])[["Amount"]].sum().reset_index()

    fish = df["Amount"].sum()

    return fish

# %%
main2(test, 256)

# %%
main2(sample, 256)
# %%
