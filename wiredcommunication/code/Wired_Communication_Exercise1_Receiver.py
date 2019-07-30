from microbit import *

x=0
y=0
one_threshold = 100
zero_threshold = 37.5

while True:
    signal_time = None

    while(pin2.read_digital()):
        if not signal_time:
            signal_time = running_time()

    line_free_time = running_time()

    if(signal_time):
        duration = line_free_time - signal_time

        if(duration > one_threshold):
            display.set_pixel(x,y,9)

        if(duration > zero_threshold):
            x=x+1
            if(x>4):
                x=0
                y=y+1
            if(y>4):
                y=0
                x=0
        else:
            pass

    if button_a.is_pressed():
        display.clear()
