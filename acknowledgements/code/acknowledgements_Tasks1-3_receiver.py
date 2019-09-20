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

### TASK 1 ###
my_address = "CS"
their_address = "JG"
header = my_address + their_address

acknowledge_string = "ACK"
acknowledge_packet = header + acknowledge_string

error = 25

### TASK 2 ###
data_received = {}

# Adds data received to data_received
# Sends back an acknowledgment after every message received
while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[2:4] == my_address:
            data = message[4:]

        # Send with error
        sendWithError(acknowledge_packet,error)

             
        if data != "Start" and data != "End":
            
            data_received["data"] += 1
        elif data == "End":
                data_uniques = list(dict.fromkeys(data_received))
                duplicates = len(data_received) - len(data_uniques)
                display.scroll(str(duplicates))
                data_received = []
            
            message = None