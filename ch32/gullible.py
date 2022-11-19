"""Gullible, by Jake Dobler jaecob.d1@gmail.com"""

print('Gullible, by Jake Dobler jaecob.d1@gmail.com')

while True: # Main program loop.
    print("Do you want to know how to keep a gullible person busy for hours? Y/N")
    response = input('> ') # Get the user's response.
    if response.lower() == 'no' or response.lower() =='n':
        break # If "no", break out of this loop.
    if response.lower() == 'yes' or response.lower() == 'y':
        continue # If "yes", continue to the start of this loop
    print('"{}" is not a valid yes/no response.'.format(response))

print('Thank you. Have a nice day!')