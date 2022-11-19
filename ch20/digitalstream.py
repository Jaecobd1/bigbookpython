"""Digital Stream, by Jake Dobler jaecob.d1@gmail.com
A screensaver in the style of the Matrix's movie visuals"""

import random, shutil, sys, time, colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN)
print(Back.BLACK)
# set up the constants:
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 16
PAUSE = 0.1
STREAM_CHARS = ['0', '1']

# Density can range from 0.0 1.0:
DENSITY = 0.02

#Get the size of the terminal window:
WIDTH = shutil.get_terminal_size()[0]
# We can't print to the last column on WIndows without it adding a new line automatically
# So reduce the width by one:
WIDTH -= 1

print('Digital Stream. by Jake Dobler jaecob.d1@gmail.com')
print('Press ctr-c to quit.')
time.sleep(2)

try:
    # For each column, when the counter is 0, no stream is shown.
    # Otherwise, it acts as a counter for how many times as 1 or 0
    # should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # Set up the counter for each column:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    #Restart a stream on this column.
                    columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

                # Display an empty space or a 1/0 character.
            if columns[i]> 0:
                print(random.choice(STREAM_CHARS), end="")
                columns[i] -= 1
            else:
                print(' ', end="")
        print() # Print a newline at the end of the row of columns.
        sys.stdout.flush() # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()