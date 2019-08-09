from microbit import *
import radio
import random

radio.on()

### TASK 1 ###
my_address = "CS"
their_address = "JG"
header = my_address + their_address

acknowledge_string = "ACK"
acknowledge_packet = header + acknowledge_string

### TASK 2 ###
data_received = []

# Adds data received to data_received
# Sends back an acknowledgment after every message received
while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[:2] == their_address:
            data = message[4:]

            # There is a % chance for the acknowledgment not to be sent
            generated = random.randint(1, 100)
            if generated >= 25: # 75% chance of sending, 25% chance of not sending
                radio.send(acknowledge_packet)
                if data != "Start" and data != "End":
                    data_received.append(data)
                elif data == "End":
                    data_uniques = list(dict.fromkeys(data_received))
                    duplicates = len(data_received) - len(data_uniques)
                    display.scroll(str(duplicates))

                    data_received = []
            
            message = None