# Task 4: Left Microbit
from microbit import *

# Displays HEART until tilted right
while accelerometer.current_gesture() != "right":
        display.show(Image.HEART)

while True:
    # If tilted right, clear display and set pin1 to high
    # Otherwise set pin1 low
    if accelerometer.current_gesture() == "right":
        pin1.write_digital(1)
        display.clear()
    else:
        pin1.write_digital(0)
    
    # If pin2 is high, display a heart    
    signal = pin2.read_digital()     
    if signal == 1:
        display.show(Image.HEART)
