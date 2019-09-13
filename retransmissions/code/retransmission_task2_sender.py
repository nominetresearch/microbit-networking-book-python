from microbit import *
import random
import radio

radio.on()

# Send a message with error
def sendWithError(message, error):
    generated = random.randint(1, 100)
    if generated > error:
        radio.send(message)
        return True
    return False


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
            sendWithError(packet, 20)
            sleep(100)

        radio.send(header + "E")
        sleep(100)