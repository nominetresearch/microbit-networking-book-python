from microbit import *
import radio

# Turn radio on
radio.on()

# The line below can be used to change the radio group,
# it is already set to 0 by default but can be reconfigured to a number from 0-255
#radio.config(group = 0)

# Create the header 
# For the Ping receiver, this header should be changed to 
# me="PO" and receiver="PI"
me = "PI"
receiver = "PO"
#header: sender + receiver
header = me + receiver

while True:
    if button_a.was_pressed():
        # Send message
        send_time = running_time()
        message = "ping"
        packet = header + message
        radio.send(packet)

    #Wait for receiving messages, check what type of message received
    incoming = radio.receive()
    if incoming is not None:
            #Check if message is for me
            if len(incoming) >= 4 and incoming[2:4] == me:
                #Check if message is pong
                if(incoming[4:]=="pong"):
                    receive_time = running_time()
                    round_trip_time = receive_time - send_time
                    display.scroll(round_trip_time)
                #Check if message is ping
                elif(incoming[4:]=="ping"):
                    message = "pong"
                    packet = header + message
                    radio.send(packet)

                    