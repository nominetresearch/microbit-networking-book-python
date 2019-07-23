from microbit import *
import time

# Represents a heart, a 9 will turn an led on and a 0 will turn an led off
heart_data = [0,9,0,9,0,
            9,9,9,9,9,
            9,9,9,9,9,
            0,9,9,9,0,
            0,0,9,0,0]

while True:
    pin1.write_digital(0)
    x = 0
    y = 0
    # Once A is pressed displays a heart for a second, writes high to pin1 and begins the animation
    if button_a.is_pressed():
        display.show(Image.HEART)
        sleep(1000)
        pin1.write_digital(1)
        sleep(100)

        # Turns each of the pixels off row by row
        for i in heart_data:
            display.set_pixel(x, y, 0)
            
            x += 1
            if x == 5:
                x = 0
                y += 1
            sleep(100)
