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

while True:
    if button_a.is_pressed():
        # Send message
        send_time = running_time()
        radio.send(packet)

        # When a message is received, calculate and display the round trip time
        received = False
        while received == False:
            incoming = radio.receive()
            if incoming is not None:
                if len(incoming) >= 4:
                    received = True
        
        receive_time = running_time()
        round_trip_time = receive_time - send_time

        incoming = ""
        display.scroll(round_trip_time)
            