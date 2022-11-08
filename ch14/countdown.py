"""Countdown, by Jake Dobler jaecob.d1@gmail.com

Show a countdown timer animation using a seven-segment display.
Press Ctrl-C to Stop."""

import sys, time
import sevseg #Imports our sevseg.py program.

secondsLeft = 3000

try:
    while True: # Main program loop.
        #Clear the screen by printing several new lines:
        print('\n' * 60)

        #Get the hours/minutes/seconds from secondsLeft:
        # For example: 7265 is 2 hours, 1 minute, 5 seconds.
        # so 7265 // 3600 is 2 hours:
        hours = str(secondsLeft // 3600)
        # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
        minutes = str((secondsLeft % 3600) // 60)
        #And 7265 % 60 is 5 seconds:
        seconds = str(secondsLeft % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()
        
        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTowRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomwRow = sDigits.splitlines()

        #Display the digits:
        print(hTopRow + '   ' + mTowRow + '  ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow) 
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomwRow)

        if secondsLeft == 0:
            print()
            print('  ****BOOM**** ')
            break
        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1) # Insert a one-second pause.
        secondsLeft -= 1

except KeyboardInterrupt:
    print('Countdown, by Jake Dobler jaecob.d1@Gmail.com')            
    sys.exit() # When Ctrl + C is pressed, end the program.