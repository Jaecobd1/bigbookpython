"""Deep Cave, by Jake Dobler jaecob.d1@Gmail.com"""

import random, sys, time

# Set up the constants:
WIDTH = 70
PAUSE_AMOUNT = 0.05

print('Deep Cave, by Jake Dobler')
print('Press Ctrl-c to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 10

while True:
    # Display the tunnel segment:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth)+('#' * rightWidth))
    #Check for Ctrol-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit() # When Ctrl-c is pressed, end the program

    #Adjust the left side width:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth -1 
    elif diceRoll == 2 and leftWidth +gapWidth < WIDTH -1:
        leftWidth = leftWidth + 1 
    else:
        pass

    