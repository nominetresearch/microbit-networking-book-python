from microbit import *
import radio
import random

radio.on()
# List of strings that could be sent
stringlist = ["Message received!", "Incoming message!", "New message sent!", "Hello"]

while True:
    # Chooses a random number from 0-9 to send over radio
    if button_a.is_pressed():
        number = str(random.randint(0, 9))
        radio.send(number)
        # Holding down the button, or not releasing the button fast enough would cause multiple messages to be sent
        # To avoid this, add a sleep after each button press
        sleep(1000)
    # Chooses a random string to send by radio
    elif button_b.is_pressed(): # Don't want both buttons being pushed simultaneously, thus elif
        string = random.choice(stringlist)
        radio.send(string)
        sleep(1000)