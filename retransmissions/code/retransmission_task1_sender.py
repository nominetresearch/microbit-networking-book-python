from microbit import *
import random
import radio

radio.on()

#expects string to send
def sendWithError(message, error):
    generated = random.randint(1,100)
    if generated <= error:
        sent = True
    else:
        sent = False

    if sent == False:
        radio.send(message)

    return sent

my_address = "JG"
their_address = "CS"
header = my_address + their_address

# Send packet with error when A is pressed
while True:
    if button_a.is_pressed():
        number_chosen = random.randint(0, 9)
        packet = header + str(number_chosen)
        
        sendWithError(packet, 20)
        sleep(500)