"""Dice Math, by Jake Dobler jaecob.d1@gmail.com
A flashcard addition game where you sum the total on random dice rolls"""

import random, time

# Set up the constants:
DICE_WIDTH =  9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79

CANVAS_HEIGHT = 24 - 3 

# The duration is in seconds
QUIZ_DURATION = 30
MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
PENALTY = 1

# The program hangs if all of the dice can't fit on the screen:
assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   0   |',
       '|       |'
       '+-------+'], 1)

D2a = (['+-------+',
        '| 0     |',
        '|       |',
        '|     0 |',
        '+-------+'],2)

D2b = (['+-------+',
        '|     0 |',
        '|       |',
        '| 0     |',
        '+-------+'],2)

D3a = (['+-------+',
        '| 0     |',
        '|   0   |',
        '|     0 |',
        '+-------+'],3)

D3a = (['+-------+',
        '|     0 |',
        '|   0   |',
        '| 0     |',
        '+-------+'],3)

D4 = ([ '+-------+',
        '| 0   0 |',
        '|       |',
        '| 0   0 |',
        '+-------+'],4)
D5 = ([ '+-------+',
        '| 0   0 |',
        '|   0   |',
        '| 0   0 |',
        '+-------+'],5)

D6a = (['+-------+',
        '| 0   0 |',
        '| 0   0 |',
        '| 0   0 |',
        '+-------+'],6)

D6b = (['+-------+',
        '| 0 0 0 |',
        '|       |',
        '| 0 0 0 |',
        '+-------+'],6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print('''Dice Math, by Jake Dobler jaecob.d1@gmail.com

Add up the sides of all the dice displayed on the screen. You have {} seconds to answer as many possible. You get {} points for each correct answer and lost {} point for each incorrect answer.
'''.format(QUIZ_DURATION, REWARD, PENALTY))
input('Press Enter to begin...')

# Keep track of how many answers were correct and incorrect:
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION: # Main game loop.
    #Come up with the dice to display:
    sumAnswer = 0
    diceFaces = []

    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        die= random.choice(ALL_DICE)
        # die[0] contains the list of strings of the die face:
        diceFaces.append(die[0])
        #die[1] contains the integer number of pips on the face:
        sumAnswer += die[1]

    #Contains (x,y) tuples of the top-left corner of each die.
    topLeftDiceCorners = []

    # Figure out where dice should go:
    for i in range(len(diceFaces)):
        while True:
            #Find a random place on the canvas to put the die:
            left = random.randint(0, CANVAS_WIDTH - 1 -DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT -1 - DICE_HEIGHT)

            # Get the x, y coordinates for all four corners:
            #     Left
            #     V
            #TOP >  +-------+ ^
            #       | 0     | |
            #       |   0   | DICE_HEIGHT (5)
            #       |     0 | |
            #       +-------+ v
            #       <------->
            #        DICE_WIDTH (9)
            topLeftX = left
            topLeftY = top
            topRightX = left + DICE_WIDTH
            topRightY = top
            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT
            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            #Check if this die overlaps with previous dice.
            overlaps = False
            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                prevDieRight = prevDieLeft + DICE_WIDTH    
                prevDieBottom = prevDieTop + DICE_HEIGHT
                # Check each corner of this die to see if it is inside of the area the previous die:
                for cornerX, cornerY in (
                    (topLeftX, topLeftY),
                    (topRightX, topRightY), (bottomLeftX, bottomLeftY),
                    (bottomRightX, bottomRightY)):
                    if (prevDieLeft <= cornerX < prevDieRight and prevDieTop <= cornerY < prevDieBottom):
                        overlaps = True
                if not overlaps:
                    # It doesn't overlap, so we can put it here:
                    topLeftDieCorners.append((left, top))
                    break

        #Draw the dice on the canvas:

        #Keys are (x, y) tuples of ints, values the character at that position on the canvas:
        canvas = {}
        # Loop over each die:
        for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
            # Loop over each character in the die's face:
            dieFace = diceFaces[i]
            for dx in range(DICE_WIDTH):
                for dy in range(DICE_HEIGHT):
                    # Copy this character to the correct place on the canvas:
                    canvasX = dieLeft + dx
                    canvasY = dieTop + dy
                    # Note that in dieFace, a list of strings, the x and y are swapped:
                    canvas[(canvasX, canvasY)]= dieFace[dy][dx]

        # Display the canvas on the screen:
        for cy in range(CANVAS_HEIGHT):
            for cx in range(CANVAS_WIDTH):
                print(canvas.get((cx , cy), ' '), end='')