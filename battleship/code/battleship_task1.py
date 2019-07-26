from microbit import *
import radio
import random

radio.on()

my_address = "JG"
their_address = "CS"
header = my_address + their_address

# The line below will work in python 3.7 but not on the microbit as its own random module does not contain sample
#ship_positions = random.sample(range(20), 5)

# Use this code instead which randomises positions for 5 ships and avoids any overlapping
ship_positions = []
for i in range(5):
    displayed = False
    while displayed == False:
        number = random.randint(0, 19)
        if number not in ship_positions:
            ship_positions.append(number)
            displayed = True

# Displays 5 ships across rows 1-4
ship_coordinates = [] # The coordinates of each ship are added as a tuple to this list
for ship in ship_positions:
    if ship <= 4:
        display.set_pixel(ship, 1, 9)
        ship_coordinates.append((ship, 1))
    elif ship > 4 and ship <= 9:
        display.set_pixel(ship - 5, 2, 9)
        ship_coordinates.append((ship - 5, 2))
    elif ship > 9 and ship <= 14:
        display.set_pixel(ship - 10, 3, 9)
        ship_coordinates.append((ship - 10, 3))
    else:
        display.set_pixel(ship - 15, 4, 9)
        ship_coordinates.append((ship - 15, 4))
