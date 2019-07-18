# Task 4 Microbit 1
from microbit import *

# Displays on this microbit initially until it tilts right
while accelerometer.current_gesture() != "right":
        display.show(Image.HEART)

while True:
    # If tilting right, clears display and sets pin1 to high
    if accelerometer.current_gesture() == "right":
        pin1.write_digital(1)
        display.clear()
    else:
        pin1.write_digital(0)
    
    # If pin2 is high, display a heart    
    signal = pin2.read_digital()     
    if signal == 1:
        display.show(Image.HEART)
