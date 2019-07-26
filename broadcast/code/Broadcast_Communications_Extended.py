from microbit import *
import radio

radio.on()
sad = True

while True:
    if sad == True:
        display.show(Image.SAD)
    # Searches for a message, and scrolls it once it has been received
    message = radio.receive()
    if message is not None: # Can only display a message if one has been received
        display.scroll(message)
        if message == "Hello":
            display.show(Image.HAPPY)
            sleep(2000)
            display.clear()
            sad = False
