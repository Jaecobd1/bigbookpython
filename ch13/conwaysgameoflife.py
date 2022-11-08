""""Conway's Game of Life, by Jake Dobler jaecob.d1@gmail.com
The classic cellular automata simulation. Press Ctrl-C to stop.
"""

import copy, random, sys, time

# Set up the constants:
WIDTH = 79 # The Width of the cell grid.
HEIGHT = 20 # The height of the cell grid.

ALIVE = '0' # The character representing a living cell.
DEAD = '' # The character representing a dead cell.

# The cells and nextCells are dictionaries for the state of the gaame.
# Their keys are (x , y) tuples and their values are one of the Alive
# Or Dead values.
nextCells={}
# Put random dead and alive cells into nextCells:
for x in range(WIDTH): # Loop over every possible column. 
    for y in range(HEIGHT): # Loop over every possible row.
        # 50/50 change for starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE # adding a living cell.
        else:
            nextCells[(x, y)] = DEAD # Add a dead cell.
while True: #Main program loop
    # Each iteration of this loop is a step of the simulation.

    print('\n' * 50) # Separate each step with newlines.
    cells = copy.deepcopy(nextCells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x,y)], end='') # Print the # or space.
        print() #Print a newline at the end of the row.
    print('Press Ctrl-C to quit.')

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates of (x, y), even if they
            # wrap around the edges:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1 # Top-left neightbor is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1 # Top neighbor is alive.
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1 # Top-right neighbor is alive.
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1 # Left neighbor is alive.
            if cells[(right, y )] == ALIVE:
                numNeighbors += 1 # Right neightbor is alive
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1

            # Set cell based on Conway's Game of Life rules:
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[(x, y)] = ALIVE
            else:
                #Everything else dies or stays dead:
                nextCells[(x, y)] = DEAD
            
    try:
        time.sleep(1) # add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print('Conway\'s Game of life')
        print('By Jake Dobler jaecob.d1@gmail.com')
        sys.exit() # When Ctrl+C is pressed, end program