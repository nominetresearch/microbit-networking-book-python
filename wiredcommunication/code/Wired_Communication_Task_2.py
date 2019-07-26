from microbit import *

#Wired communication Task 2
signal = None
while True:
    # If A is pressed, write 1 to pin1 for 100 milliseconds
    if button_a.is_pressed():
        pin1.write_digital(1) # Set pin1 to high
        sleep(100)
        pin1.write_digital(0) # Set pin1 to low
    
    # If pin2 is read as high, turn on the led at (2, 2)    
    signal = pin2.read_digital()
    if signal == 1:
        display.set_pixel(2, 2, 9) # Set led at (2,2) to a brightness of 9 (on)
    else:
        display.set_pixel(2, 2, 0) # Set led at (2,2) to a brightness of 0 (off)
