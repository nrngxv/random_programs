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
while True: # the program starts
    print("\n\n\n\n\n") # separting each line with a new line
    current_cells = copy.deepcopy(next_cells) # copying properties of next_cells

    for y in range(HEIGHT):
        for x in range(WIDTH):
           print(current_cells[x][y], end="")
        print()

    # calculating the next cell, based on the current one
    for x in range(HEIGHT):
        for y in range(WIDTH):

            #% WIDTH/HEIGHT ensure, the coords are between 0 and WIDTH/HEIGHT-1
            leftcoord = (x - 1) % WIDTH
            rightcoord = (x + 1) % WIDTH
            topcoord = (y - 1) % HEIGHT
            bottomcoord = (y + 1) % HEIGHT

            living_neighbour = 0 # the number of living neighbour

            if current_cells[leftcoord][topcoord] == "#":
                living_neighbour += 1 # adds a living cell to topleft, if the above condition is true

            if current_cells[x][topcoord] == "#":
                living_neighbour += 1



            

