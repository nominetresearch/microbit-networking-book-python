from microbit import *
import radio
import random

caught = 0
me = 0
you = 0
# This is how you define a 5x5 image on the microbit, 0 represents an led off and 9 a led on
# A colon is used to represent a new line.
# This image will be in the shape of a donkey
donkey = Image("00009:09990:99990:09090:09090")

# The radio must be turned on for the program to work
radio.on()

while True:
    # If a shake is detected change me and send a signal to the other microbit after 0-2 seconds
    # Alterntive syntax: 'if accelerometer.current_gesture() == "shake":' however this has caused issues with the microbit screen flickering,
    # to avoid use the line below instead
    if accelerometer.was_gesture("shake"):
        if caught != 0:
            me += running_time() - caught
            display.clear()
            sleep(random.randrange(0, 2000))
        radio.send(str(me))
    
    # Checks if the radio has received something and if it has whether it is an integer
    # Then changes you and displays the donkey
    number = radio.receive()
    if number is not None:
        if number.isdigit() == True:
            caught = running_time()
            you += int(number)
            display.show(donkey)

    # Displays happy face if you win, or sad face if you lose
    if button_a.is_pressed():
        sleep(1000) # Unsure why this line is required, but when absent it can cause both microbits to display a happy face
        if me > you:
            display.show(Image.SAD)
        else:
            display.show(Image.HAPPY)
        
        me = 0
        you = 0
        caught = 0