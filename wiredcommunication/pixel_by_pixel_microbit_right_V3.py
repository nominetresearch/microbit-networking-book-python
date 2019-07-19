from microbit import *
import time

heart_data = [0,9,0,9,0,
            9,9,9,9,9,
            9,9,9,9,9,
            0,9,9,9,0,
            0,0,9,0,0]

while True:
    x = 0
    y = 0

    signal = 0
    while signal == 0:
        signal = pin2.read_digital()
        if signal == 1:
            sleep(100)

            for i in heart_data:
                if i == 9:
                    display.set_pixel(x, y, 9)

                x += 1
                if x == 5:
                    x = 0
                    y += 1
                sleep(100)

    while button_a.is_pressed() == False:
        if button_a.is_pressed():
            display.clear()