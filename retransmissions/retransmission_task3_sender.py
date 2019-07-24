from microbit import *
import random
import radio

radio.on()

def sendNumberWithError(number, chance):
    generated = random.randint(1,100)
    if generated <= chance:
        sent = True
    else:
        sent = False

    if sent == False:
        radio.send(str(number))

    return sent

# Sends a string with a % chance of failure
# Returns whether the message was sent succesfully
def sendStringWithError(string, chance):
    generated = random.randint(1,100)
    if generated <= chance:
        sent = True
    else:
        sent = False

    if sent == False:
        radio.send(string)

    return sent

def sendValueWithError(string, number, chance):
    generated = random.randint(1,100)
    if generated <= chance:
        sent = True
    else:
        sent = False

    if sent == False:
        radio.send(string + str(number))

    return sent

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
                sendStringWithError(packet, 75)
                sleep(100)

        radio.send(header + "End")
        sleep(100)