from microbit import *
import radio

radio.on()

my_address = "CS"
their_address = "JG"

# Displays number when received
while True:
    message = radio.receive()
    if message is not None:
        if len(message) == 5 and message[:2] == their_address:
            display.show(message[4])
            sleep(3000)
            display.clear()

            message = None