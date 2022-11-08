"""Sevseg, by Jake Dobler jaecob.d1@gmail.com
A seven-segment number display module, used by the Countdown and Digital Clock programs."""

"""A labeled seven-segment display, with each segment laeled A to G:
 _A_ 
|   |
F   B
|_G_|       Each Digit in a seven-segment display:
|   |        __          __   ___    
E   C       |  |   |     __|  ___|   |__|
|_D_|       |__|   |    |__   ___|      |         """   

def getSevSegStr(number, minWidth=0):
    """Return a seven-segment display string of number. The Returned
    string will be padded with zeros if it is smaller than minWidth."""

    # Convert number to string in case it's an int or float:
    number = str(number).zfill(minWidth)

    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if number == '.': # Render the decimal point.
            rows[0] += ''
            rows[1] += ' '
            rows[2] += '. '
            continue # Skip the space in between digits
        elif numeral == '-': # Render the negative sign:
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '1': # Render the 1.
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2': # Render the 2
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__'
        elif numeral == '3': # Render the 3
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4': # Render the 4
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':
            rows[0] += ' __ '
            rows[1] += '|__'
            rows[2] += ' __|'
        elif numeral == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '   |'

        # Add a space ( for the space inbetween numerals) if this isn't the last numeral:
        if i != len(number) -1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '
            return '\n'.join(rows)


#If this program isn't being imported, display the numbers 00 to 00.
if __name__ == '__main__':
    print('This module is meant to be imported rather than run.')
    print('For example, this code:')
    print('  import sevseg')
    print('   myNumber = sevseg.getSevSegStr(42, 3)')
    print('   print(myNumber)')
    print()
    print('...will print 42, zero-padded to three digits: ')
    print(' __        __ ')
    print('|  | |__|  __|')
    print('|__|    | |__ ')
