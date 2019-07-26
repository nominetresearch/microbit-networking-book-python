# Task 4: Right Microbit
from microbit import *

# Display nothing until a HEART is received from the Left Microbit
signal = 0
while signal != 1:
    signal = pin2.read_digital()

while True:
    # If tilted left, clear display and set pin1 to high
    # Otherwise set pin1 to 0
    if accelerometer.current_gesture() == "left":
        pin1.write_digital(1)
        display.clear()
    else:
        pin1.write_digital(0)

    # If pin2 is high, display a heart  
    signal = pin2.read_digital()  
    if signal == 1:
        display.show(Image.HEART)
