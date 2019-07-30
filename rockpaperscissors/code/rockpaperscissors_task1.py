from microbit import *
import random

# Images for rock, paper and scissors
rock = Image("00000:09990:09990:09990:00000")
paper = Image("99999:90009:90009:90009:99999")
scissors = Image("99009:99090:00900:99090:99009")

while True:
    if accelerometer.was_gesture("shake"):
        hand = random.randint(1,3)
        if hand == 1:
            display.show(paper)
        elif hand == 2:
            display.show(rock)
        else:
            display.show(scissors)

