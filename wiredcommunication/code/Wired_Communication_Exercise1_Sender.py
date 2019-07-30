from microbit import *
import microbit

# 2nd Micro:bit does not start with displaying a heart icon
heart=[0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0]
x=0
y=0
start = False
index=0

# Do always

while True:
    if button_a.is_pressed():
        display.show(Image.HEART)
        sleep(2000)
        start = True

    if start:
        index=0
        while(index < 25):
            if(heart[index]==1):
                pin1.write_digital(1)
                sleep(137.5)
            else:
                pin1.write_digital(1)
                sleep(62.5)
            pin1.write_digital(0)
            sleep(25)
            y=index//5
            x=index%5
            microbit.display.set_pixel(x, y, 0)
            index=index+1
        start=False