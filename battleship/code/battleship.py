from microbit import *
import radio
import random

radio.on()

my_address = "CS"
their_address = "JG"
header = my_address + their_address

# Pick random positions for 5 ships avoiding any overlapping
ship_positions = []
for i in range(5):
    displayed = False
    while not displayed:
        number = random.randint(5, 24)
        if number not in ship_positions:
            ship_positions.append(number)
            displayed = True

# Displays 5 ships across rows 1-4
# The coordinates of each ship are added as a tuple to this list
def display_ships():
    display.clear()
    for ship in ship_positions:
        ship_y = int(ship/5)
        ship_x = ship-ship_y*5
        display.set_pixel(ship_x, ship_y, 9)
   
# initialize counters
fire_x = 0
fire_y = 1
hit_count = 0

# Keeps hold of score
my_hits = 0
their_hits = 0

show_ships = True
shoot = False

while True:
    if show_ships:
        display_ships()
    # fire_x is the column number of shot, and determined by button_a presses
    # fire_y is the row number of shot, determined by button_b presses
    # we send the index in the array where the shot is aimed
    # the code checks accepts buttons a and b pressed one after the other within 200ms
    # otherwise it is hard to get both buttons pressed at the same time
    if button_a.was_pressed() and not button_b.was_pressed():
        sleep(200)
        if button_b.was_pressed():
            shoot = True
        else:
            show_ships = False
            display.clear()
            fire_x += 1
            if fire_x >= 5:
                fire_x = 0
            display.set_pixel(fire_x, fire_y, 9)
    elif button_b.was_pressed() and not button_a.was_pressed():
        sleep(200)
        if button_a.was_pressed():
            shoot = True
        else:
            show_ships = False
            display.clear()
            fire_y += 1
            if fire_y >= 5:
                fire_y = 1
            display.set_pixel(fire_x, fire_y, 9)
     
    # If both buttons are pressed at the same time, send the chosen 
    # coordinate to the opponent
    if shoot or (button_a.is_pressed() and button_b.is_pressed()):
        show_ships = True
        shoot = False
        radio.send(str(fire_x + 5 * fire_y))
        sleep(500)
        
    # Check if packet received
    incoming = radio.receive()
    if incoming:
        # if it is a miss, just turn on the pixel on (4, 0)
        # But (0, 0) pixel may be already on, so turn it off
        if incoming == "Miss":
            display.set_pixel(4, 0, 9)
            sleep(500)
            display.set_pixel(0, 0, 0)
        # if it is a hit, turn on the pixel on (0, 0)
        # but (4, 0) pixel may be already on, so turn it off
        # incraese the hit count
        # if we reached 5, we won - display HAPPY! Game over
        elif incoming == "Hit":
            hit_count = hit_count + 1
            display.set_pixel(0, 0, 9)
            sleep(500)
            display.set_pixel(4, 0, 0)
            if hit_count == 5:
                display.show(Image.HAPPY)
                show_ships = False
        # otherwise we received a number
        # if we have a submarine in that location:
        # remove it from our ship list
        # send "Hit"
        # if the opponent missed:
        # send "Miss"
        else:
            index = int(incoming)
            if index in ship_positions:
                ship_positions.remove(index)
                radio.send("Hit")
            else:
                radio.send("Miss")