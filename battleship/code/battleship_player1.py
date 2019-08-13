from microbit import *
import radio
import random

radio.on()

my_address = "JG"
their_address = "CS"
header = my_address + their_address

# Pick random positions for 5 ships avoiding any overlapping
ship_positions = []
for i in range(5):
    displayed = False
    while displayed == False:
        number = random.randint(5, 24)
        if number not in ship_positions:
            ship_positions.append(number)
            displayed = True

# Displays 5 ships across rows 1-4
# The coordinates of each ship are added as a tuple to this list
#TODO: This can be better done with using modulo
ship_coordinates = [] 
for ship in ship_positions:
    ship_x = int(ship/5)
    ship_y = ship-ship_x*5
    display.set_pixel(ship_y, ship_x)
    ship_coordinates.append((ship_y,ship_x))

# Sets the coordinates to fire at
row_number = 0
column_number = -1
selected = False

# Keeps hold of score
my_hits = 0
their_hits = 0

while True:
    # When A or B is first pressed, the led at (0,1) turns on
    # Use A and B to change the selected column or row, 
    # the led for that coordinate will light up
    # If A and B are both pressed together, 
    # the shot is fired to the other microbit 
    # and your ships will be visible again
    while selected == False:

        # This checks to see if B is also pressed and fires the shot 
        # if it is, or increments column if not
        if button_a.is_pressed():
            other_button_pressed = False
            if row_number == 0:
                row_number = 1
            else:
                time_passed = 0
                while time_passed <= 250 and other_button_pressed == False:
                    if button_b.is_pressed():
                        other_button_pressed = True
                    else:
                        time_passed += 5
                        sleep(5)

            if other_button_pressed == True:
                packet = header + str(column_number) + str(row_number)
                radio.send(packet)

                display.clear()
                for i in ship_coordinates:
                    display.set_pixel(i[0], i[1], 9)

                row_number = 0
                column_number = -1
                selected = True
            else:
                display.clear()
                column_number += 1
                if column_number == 5:
                    column_number = 0
                display.set_pixel(column_number, row_number, 9)
                sleep(250)

        # This checks to see if A is also pressed and fires the shot if it is, or increments row if not
        elif button_b.is_pressed():
            other_button_pressed = False
            if column_number == -1:
                column_number = 0
            else:
                time_passed = 0
                while time_passed <= 250 and other_button_pressed == False:
                    if button_a.is_pressed():
                        other_button_pressed = True
                    else:
                        time_passed += 5
                        sleep(5)

            if other_button_pressed == True:
                packet = header + str(column_number) + str(row_number)
                radio.send(packet)

                display.clear()
                for i in ship_coordinates:
                    display.set_pixel(i[0], i[1], 9)

                row_number = 0
                column_number = -1
                selected = True
            else:
                display.clear()
                row_number += 1
                if row_number == 5:
                    row_number = 1

                display.set_pixel(column_number, row_number, 9)
                sleep(250)

    while selected == True:
        message = radio.receive()
        if message is not None:
            # Check to see if the message received was a shot your opponent fired, and if it is:
            # If it hit, remove ship from the display and tell them it was a hit
            # If it missed tell them it missed
            if len(message) == 6 and message[:2] == their_address and message[2:4] == my_address:
                # Turns off the hit/miss leds when your opponents shot is received
                display.set_pixel(0, 0, 0)
                display.set_pixel(4, 0, 0)

                column_fired = int(message[4])
                row_fired = int(message[5])
                shot = (column_fired, row_fired)

                if shot in ship_coordinates:
                    ship_coordinates.remove(shot)
                    display.set_pixel(column_fired, row_fired, 0)
                    packet = header + "H"
                    their_hits += 1
                else:
                    packet = header + "M"
                radio.send(packet)

                # Shows sad face if you lose
                if their_hits == 5:
                    while True:
                        display.show(Image.SAD)

                selected = False

            # Checks to see if the message was a hit/miss message, and if it is:
            # Turn on top left led for a hit, 5 hits and you win
            # Turns on top right led for a miss
            elif len(message) == 5 and message[:2] == their_address and message[2:4] == my_address:
                on_target = message[4]
                if on_target == "H":
                    my_hits += 1
                    display.set_pixel(0, 0, 9)
                    # Shows happy face if you win
                    if my_hits == 5:
                        while True:
                            display.show(Image.HAPPY)
                elif on_target == "M":
                    display.set_pixel(4, 0, 9)


            message = None
