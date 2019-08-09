from microbit import *
import random
import radio

radio.on()

my_address = "JG"
their_address = "CS"
header = my_address + their_address

# When A is pressed send 'start', 10 digits with error and then 'end'
while True:
    if button_a.is_pressed():
        radio.send(header + "Start")
        sleep(100)

        for digit in range(1, 11):
            packet = header + str(digit)
            for i in range(2):
                radio.send(packet)
                sleep(100)

        radio.send(header + "End")
        sleep(100)