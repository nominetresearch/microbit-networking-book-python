from microbit import *
import radio

radio.on()
#radio.config(group = )

counter = 0

while True:
    message = radio.receive()
    if message is not None: # Can only display a message if one has been received
        counter += 1
        display.scroll(message)
    
    # Note that if using the sender code from before, it will also count strings sent
    if button_a.is_pressed():
        display.show(counter)
        sleep(3000)
        display.clear()
