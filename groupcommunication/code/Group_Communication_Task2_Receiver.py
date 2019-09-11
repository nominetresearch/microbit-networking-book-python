from microbit import *
import radio

radio.on()
#radio.config(group = 1)

counter_number = 0
counter_other = 0

while True:
    message = radio.receive()
    #Check if message is received
    if message is not None: 
        if number.isdigit():
            number = int(message)
            # Check if received a number  
            if(number>=0 and number <=9):
                counter_number += 1
                display.scroll(message)
            else:
                counter_other += 1
        else:
            counter_other += 1
    
    # Note that if using the sender code from before, it will also count strings sent
    if button_a.is_pressed():
        display.show(counter_number)
        sleep(1000)
        display.show(counter_other)
        sleep(1000)
        display.clear()
