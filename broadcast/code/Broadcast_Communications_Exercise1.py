# Extended Activity - Exercise 1:

from microbit import *
import radio

# Turn radio on
radio.on()

# Do always
while True:
    # Default SAD
    display.show(Image.SAD)

    # If shaken, send a "Hello"
    if accelerometer.is_gesture('shake'):
        radio.send('Hello')

    # Listen for messages
    message = radio.receive()
    if message == 'Hello': 
        display.show(Image.HAPPY) # Show happy face 
        sleep(2000)