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

# When A is pressed send 'S', 10 numbers with error and then 'E'
while True:
    if button_a.is_pressed():
        radio.send(header + "S")
        sleep(100)

        for number in range(1, 11):
            packet = header + str(number)
            for i in range(2):
                sendWithError(packet, 75)
                sleep(100)

        radio.send(header + "E")
        sleep(100)