from microbit import *
import radio

### TASK 1 ###
# Turn radio on 
radio.on()

# The line below can be used to change the radio group,
# set to 0 by default but can be configured to  0-255
#radio.config(group = 0)

### TASK 2 ###
# Create the head have symmetric headers 
string_sender = "CS"
string_receiver = "AK"
header = string_sender + string_receiver

### TASK 3 ###
# Create the message and attach to header to form packet
message = "Hello"
packet = header + message

# Send message
radio.send(packet)

### TASK 4 ###

while True:
    # Check for messages, any of length 4 or greater will be kept
    incoming = radio.receive()
    if incoming is not None:
        if len(incoming) >= 4:
            sender_address = incoming[0:2]
            receiver_address = incoming[2:4]
            sender_message = incoming[4:]

            display.scroll(sender_address)
            sleep(1000)
            display.scroll(sender_message)