from microbit import *
import radio

# Turn radio on
radio.on()

# The line below can be used to change the radio group,
# it is already set to 0 by default but can be reconfigured to a number from 0-255

#radio.config(group = 0)

# Create the header
string_sender = "PO"
string_receiver = "PI"
header = string_sender + string_receiver

# Create the message and attach to header to form package
message = "ping"
packet = header + message

while True:
    if button_a.is_pressed():
        # Send message
        send_time = running_time()
        message = "ping"
        packet = header + message
        radio.send(packet)

        # When a message is received, 
        # calculate and display the round trip time

        #The reception loop can be improved
        received = False
        while received == False:
            incoming = radio.receive()
            if incoming is not None:
                if len(incoming) >= 4 and incoming[:2] == string_receiver and incoming[2:4] == string_sender:
                    received = True

        receive_time = running_time()
        round_trip_time = receive_time - send_time

        incoming = ""
        display.scroll(round_trip_time)

    else:
        # Checks for messages, any of length 4 or greater will be kept
        incoming = radio.receive()
        if incoming is not None:
            if len(incoming) >= 4 and incoming[:2] == string_receiver and incoming[2:4] == string_sender:
                message = "pong"
                packet = header + message
                radio.send(packet)

                incoming = ""
            