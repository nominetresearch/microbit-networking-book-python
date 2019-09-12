from microbit import *
import radio
import random

caught = 0
me = 0
you = 0

# Create the donkey image
# Define a 5x5 image on the microbit
# 0 for led off and 9 for led on
# A colon to represent a new row.
donkey = Image("00009:09990:99990:09090:09090")

# Turned on the radio
radio.on()

while True:
    # If a shake gesture was detected, change 'me' and 
    # send its value to the other micro:bit after 0-2 seconds
    if accelerometer.was_gesture("shake"):
        if caught != 0:
            me += running_time() - caught
        display.clear()
        sleep(random.randrange(0, 2000))
        radio.send(str(me))
    
    # Check if the radio has received something 
    # If  received is a number,
    # change 'you' and display the donkey
    number = radio.receive()
    if number is not None:
        if number.isdigit() == True:
            caught = running_time()
            you = int(number)
            display.show(donkey)

    # If button A is pressed, check 'me' and 'you' 
    # Display happy face 'me' is greater, and sad face othewise
    if button_a.is_pressed():
        sleep(1000) 
        if me > you:
            display.show(Image.SAD)
        else:
            display.show(Image.HAPPY)
        me = 0
        you = 0
        caught = 0