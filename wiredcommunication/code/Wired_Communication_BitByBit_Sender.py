from microbit import *
import microbit

# Heart is an array of 25 bits.
# Pixel location is x,y and i = y*5+x
heart=[0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0]
start = False

#Initialize 1 and 0 signal durations
signal_long = 140
signal_short = 65

while True:
    #Pressing button A, starts sending
    if button_a.is_pressed():
        display.show(Image.HEART)
        sleep(2000)
        start = True

    #Start sending starting from the beginning
    if start:
        index=0
        while(index < 25):
            #If 1, then send a long signal, 
            #Else, send a short signal
            if(heart[index]==1):
                pin1.write_digital(1)
                sleep(signal_long)
            else:
                pin1.write_digital(1)
                sleep(signal_short)
            pin1.write_digital(0)
            sleep(25)
            #Calculate the pixel location to turn off
            y=index//5
            x=index%5
            microbit.display.set_pixel(x, y, 0)
            #Advance to send the next bit
            index=index+1
        #Sent all, so reset
        start=False