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

# Send packet with error when A is pressed
while True:
    if button_a.is_pressed():
        number_chosen = random.randint(0, 9)
        packet = header + str(number_chosen)
        
        sendStringWithError(packet, 20)
        sleep(500)