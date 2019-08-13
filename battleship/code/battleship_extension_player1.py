# In this variation, your ships now use experimental missiles which have a high chance of exploding midair
# If this happens you won't know whether your shot was going to hit or miss
# To prevent that from happening each ship will fire multiple shots in one go at the same coordinate so hopefully atleast one will land
# This uses the concept of retransmmisons from the previous chapter

from microbit import *
import radio
import random

radio.on()

my_address = "JG"
their_address = "CS"
header = my_address + their_address

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

# Fires 'shot_count' many shots with a 'chance' % of failure
results = []
def sendShotsWithError(packet, shot_count, chance):
    shot_status = []
    for shot in range(shot_count):
        generated = random.randint(1, 100)
        if generated <= chance:
            failure = True
        else:
            failure = False

        if failure == False:
            radio.send(packet)

        shot_status.append(failure)
    
    return shot_status    

# Sets the coordinates to fire at
row_number = 0
column_number = -1
selected = False

# Keeps hold of score
my_hits = 0
their_hits = 0

while True:
    while selected == False:
        # This checks to see if B is also pressed and fires the shot if it is, or increments column if not
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
                results = sendShotsWithError(packet, 4, 75) # Sends the shots and returns the status of the shots fired


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
                results = sendShotsWithError(packet, 4, 75)

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
        # If all the shots failed, let your opponent know
        if results.count(True) == len(results) and len(results) != 0:
            packet = header + "FAIL"
            radio.send(packet)
            results = [] # Prevents this if statement from being called again until you next fire your shots
            display.set_pixel(2, 0, 9) # Turns on the middle pixel in the top row if all your shots failed

        elif message is not None:
            if len(message) == 6 and message[:2] == their_address and message[2:4] == my_address:
                # Turns off the hit/miss/failed leds when your opponents shot is received
                display.set_pixel(0, 0, 0)
                display.set_pixel(2, 0, 0)
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

                radio.off() # Reboots radio to flush receive queue
                radio.on()
                selected = False

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

            # If all your opponents shots failed, it's your turn
            elif message[4:] == "FAIL" and message[:2] == their_address and message[2:4] == my_address:
                display.set_pixel(0, 0, 0)
                display.set_pixel(2, 0, 0)
                display.set_pixel(4, 0, 0)

                selected = False

            message = None
