# Task 2:

from microbit import *
import radio

radio.on()

while True:
    # Listen for a message
    message = radio.receive()
    
    # If message received, display
    if message is not None: 
        display.scroll(message)
