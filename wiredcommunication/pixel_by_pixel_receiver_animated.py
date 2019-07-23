from microbit import *
import time

# Represents a heart, a 9 will turn an led on and a 0 will turn an led off
heart_data = [0,9,0,9,0,
            9,9,9,9,9,
            9,9,9,9,9,
            0,9,9,9,0,
            0,0,9,0,0]

while True:
    x = 0
    y = 0

    # Checks for a high signal from pin2, once received the animation begins
    signal = 0
    while signal == 0:
        signal = pin2.read_digital()
        if signal == 1:
            sleep(100)

            # Row by row turns an led on if 9 is read or off if 0 is read
            for i in heart_data:
                if i == 9:
                    display.set_pixel(x, y, 9)

                x += 1
                if x == 5:
                    x = 0
                    y += 1
                sleep(100)

    # Clears display if A is pressed
    while button_a.is_pressed() == False:
        if button_a.is_pressed():
            display.clear()
