#this is the conway game of life simulation

import random, time, copy

# setting global variables for width and height
WIDTH = 60
HEIGHT = 20

# Creating a grid, a list inside of list
next_cells = []

for x in range(WIDTH):
    column = []

for y in range(HEIGHT):
    if random.randint(0,1) == 0:
        column.append("#")
    else:
        column.append(" ")

next_cells.append(column) # adding column value to the main list


# The logic of what should happen

