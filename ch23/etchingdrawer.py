"""Etching Drawer, by Jake Dobler jaecob.d1@gmail.com"""

import shutil, sys

# Set up the constants for line characters:
UP_DOWN_CHAR = chr(9474) # Character 9474 is "|"
LEFT_RIGHT_CHAR = chr(9472)
DOWN_RIGHT_CHAR = chr(9484)
DOWN_LEFT_CHAR = chr(9488)
UP_RIGHT_CHAR = chr(9492)
UP_LEFT_CHAR = chr(9496)
UP_DOWN_RIGHT_CHAR = chr(9500)
UP_DOWN_LEFT_CHAR = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR = chr(9524)
CROSS_CHAR = chr(9532)

# Get the size of the terminal window:
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()

# We can't print to the last column on windows without it adding a new line
# automatically, so reduce the width by one:
CANVAS_WIDTH -= 1
# Leave room at the bottom few rows for the command info lines
CANVAS_HEIGHT -= 5

"""The keys for canvas will be (x,y) integer tuples for the coordinate, and the value is a set of leeters, W, A, S, D that tell what kind of line should be drawn."""
canvas = {}
cursorX = 0
cursorY = 0

def getCanvasString(canvasData, cx, cy):
    """Returns a multiline string of the line drawn in canvasData."""
    canvasStr = ''

    """canvasData is a dictionary with (x, y) tuple keys and values that are sets of 'w' 'a', 's', and or 'd' strings to show which directions the lines are drawn at each xy point."""

    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue
            # Add the line character for this point to canvasStr.
            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D']) ):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += '\n' # Add a new line at the end of each row.
    return canvasStr

moves = []

while True: # Main program loop.
    # Draw the lines based on the data in canvas:
    print(getCanvasString(canvas, cursorX, cursorY))

    print('WASD keys to move, H for help, C to clear, F to save, or Quit.')
    response = input('> ').upper()

    if response == 'QUIT':
        print('Thank you for playing!')
        sys.exit() # Quit the program
    elif response == 'H':
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and ssdddwwwaaa draws a box.')
        print()
        print('You can save your drawings to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {} # Erase the canvas data.
        moves.append('C')
    elif response == 'F':
        # Save the canvas string to a text file:
        try:
            print('Enter filename to save to:')
            filename = input('> ')

            # Make sure the filename ends with .txt:
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))

        except:
            print('Error: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue # Ignore this letter and continue to the next one.
        moves.append(command)

        # The first line we add needs to form a full line:
        if canvas == {}:
            if command in ('W', 'S'):
                # Make the first line a horizontal one:
                canvas[(cursorX, cursorY)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                # Make the first line a vertical one:
                canvas[(cursorX, cursorY)] = set(['A', 'D'])
        
        # Update x and y:
        if command == 'W' and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY -1
        elif command == 'S' and cursorY < CANVAS_HEIGHT -1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY + 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX -1
        elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX + 1
        else:
            # If the cursor doesn't move because it would have moved off
            # the edge of the canvas, then don't change the set at
            # canvas[(cursorX, cursorY)].
            continue
        # If there's no set for (cursorX, cursorY), add and empty set:
        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        # Add the direction string to this xy point's set:
        if command == 'W':
            canvas[(cursorX, cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX, cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX, cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX, cursorY)].add('A')


            
