from microbit import *

# This is built to follow the micro block diagram in task 2
signal = None
while True:
    # If A is pressed, right to pin1 for 0.1 seconds
    if button_a.is_pressed():
        pin1.write_digital(1) # Sets pin 1 to high
        sleep(100)
        pin1.write_digital(0) # Sets pin 1 to low
    
    # If pin2 is read as high, it will turn on the led at (2, 2)    
    signal = pin2.read_digital()
    if signal == 1:
        display.set_pixel(2, 2, 9) # Sets led at (2,2) to a brightness of 9 (on)
    else:
        display.set_pixel(2, 2, 0) # Sets led at (2,2) to a brightness of 0 (off)
