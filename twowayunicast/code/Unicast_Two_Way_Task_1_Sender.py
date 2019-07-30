from microbit import *
import radio

# Turns radio on - this must be stated in the code
radio.on()

# The line below can be used to change the radio group,
# it is already set to 0 by default but can be reconfigured to a number from 0-255

#radio.config(group = 0)

# Create the header
string_sender = "PI"
string_receiver = "PO"
header = string_sender + string_receiver

# Create the message and attach to header to form package
message = "ping"
packet = header + message
