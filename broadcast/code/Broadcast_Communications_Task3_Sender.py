# Task 3:

from microbit import *
import radio
import random

radio.on()
# List of strings that can be sent
stringlist = ["Message received!", "Incoming message!", "New message!", "Hello"]

while True:
    # Press button A to send a number
    if button_a.is_pressed():
        # Choose a random number between 0-9 
        number = str(random.randint(0, 9))
        radio.send(number)
        sleep(1000)
    # Press button B to choose a random string to send
    elif button_b.is_pressed(): 
        string = random.choice(stringlist)
        radio.send(string)
        sleep(1000)