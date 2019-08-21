from microbit import *

#Initialise pixel coordinates x,y
x=0
y=0

#Pick signal duration thresholds for 1 and 0
one_threshold = 100

while True:

    #Initialise to not receiving a signal
    signal_time = None

    #Read pin2
    while(pin2.read_digital()):
        #If pin2 is 1, mark this as signal start
        if not signal_time:
            signal_time = running_time()

    #Mark the time the signal switches to 0
    line_free_time = running_time()

    #If you detected a signal, calculate its duration
    if(signal_time):
        duration = line_free_time - signal_time

        #If duration is greater than one_threshold,received 1. 
        #Turn on the pixel at x,y
        if(duration > one_threshold):
            display.set_pixel(x,y,9)

        #Advance the pixel location to next pixel
        #If x > 4, then need to set x=0, to receive next row
        #If y>4, all rows received, reset x,y both to 0
        x=x+1
        if(x>4):
            x=0
            y=y+1
        if(y>4):
            y=0
            x=0

    #Pressing button A, clears display
    if button_a.is_pressed():
        display.clear()
