from microbit import *
import radio

# Turns radio on - this must be stated in the code
radio.on()

# The line below can be used to change the radio group,
# it is already set to 0 by default but can be reconfigured to a number from 0-255

#radio.config(group = 0)

# Create the header
string_sender = "PO"
string_receiver = "PI"
header = string_sender + string_receiver

# Create the message and attach to header to form package
message = "pong"
packet = header + message

while True:
    # Checks for messages, any of length 4 or greater will be kept
    incoming = radio.receive()
    if incoming is not None:
        if len(incoming) >= 4:
            radio.send(packet)

            sender_address = incoming[0:2]
            receiver_address = incoming[2:4]
            sender_message = incoming[4:]

            incoming = ""