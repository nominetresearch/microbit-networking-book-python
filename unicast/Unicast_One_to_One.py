from microbit import *
import radio

### TASK 1 ###

# Turns radio on - this must be stated in the code
radio.on()

# The line below can be used to change the radio group,
# it is already set to 0 by default but can be reconfigured to a number from 0-255

#radio.config(group = 0)

### TASK 2 ###

# Create the header
string_sender = "CS"
string_receiver = "AK"
header = string_sender + string_receiver

### TASK 3 ###

# Create the message and attach to header to form package
message = "Hello"
packet = header + message

# Send message
radio.send(packet)

### TASK 4 ###

while True:
    # Checks for messages, any of length 4 or greater will be kept
    incoming = radio.receive()
    if incoming is not None:
        if len(incoming) >= 4:
            sender_address = incoming[0:2]
            receiver_address = incoming[2:4]
            sender_message = incoming[4:]

            display.scroll(sender_address)
            sleep(1000)
            display.scroll(sender_message)