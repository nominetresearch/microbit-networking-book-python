from microbit import *
import radio
import random

radio.on()

# Sends a string with a % chance of failure
# Returns whether the message was sent succesfully
# Send a message with error
def sendWithError(message, error):
    generated = random.randint(1, 100)
    if generated > error:
        radio.send(message)
        return True
    return False

# TASK 1 #
my_address = "CS"
their_address = "JG"
header = my_address + their_address

acknowledge_string = "ACK"
acknowledge_packet = header + acknowledge_string

error = 25

# TASK 2 #
last_received = None
duplicates = 0

# Adds data received to data_received
# Sends back an acknowledgment after every message received
while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[2:4] == my_address:
            data = message[4:]
            display.scroll(data)
            # Send with error
            sendWithError(acknowledge_packet, error)
            if data != last_received:
                last_received = data
            else:
                duplicates += 1
        message = None

    if button_a.was_pressed():
        display.scroll(str(duplicates))