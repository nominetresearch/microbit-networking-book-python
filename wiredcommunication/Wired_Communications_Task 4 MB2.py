# Task 4 Microbit 2
from microbit import *

# Prevents anything from being displayed on this microbit until the other microbit tilts right
signal = 0
while signal != 1:
    signal = pin2.read_digital()

while True:
    # If tilting left, clears display and sets pin1 to high
    if accelerometer.current_gesture() == "left":
        pin1.write_digital(1)
        display.clear()
    else:
        pin1.write_digital(0)

    # If pin2 is high, display a heart  
    signal = pin2.read_digital()  
    if signal == 1:
        display.show(Image.HEART)
