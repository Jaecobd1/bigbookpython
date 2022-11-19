"""DNA, by Jake Dobler jaecob.d1@gmail.com"""

import random, sys, time
PAUSE = 0.15 

# These are the individual rows of the DNA animation:
ROWS = [
    #123456789
    '         ##', # Index 0 has no {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '     #{}------{}#',
    '     #{}-----{}#',
    '      #{}---{}#'
    '      #{}-{}#',
    '       ##',
    '      #{}-{}#',
    '      #{}---{}#',
    '     #{}-----{}#',
    '     #{}-----{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']
    #123456789 <- use this to measure the number of spaces:
try:
    print('DNA Animation, by Jake Dobler jaecob.d1@gmail.com ')
    time.sleep(2)
    rowIndex = 0

    while True: # Main program loop.
        
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0
        # Increment rowIndex to draw next row:

        #Row indexes 0 and 9 don't have nucleotides:
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # Select random nucleotide pairs, guanine-cytosine and adenine-tymine:
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = "A", "T"
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE)

except KeyboardInterrupt:
    sys.exit()