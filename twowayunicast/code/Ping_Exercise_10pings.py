from microbit import *
import radio

# Turn radio on 
radio.on()

# The line below can be used to change the radio group,
# it is already set to 0 by default 
# but can be reconfigured to a number from 0-255
# radio.config(group = 0)

# Create the header 
# For the Ping receiver, this header should be changed to 
# me="PO" and receiver="PI"
me = "PI"
receiver = "PO"
header = me + receiver

# Create the message and attach to header to form package
message = "ping"
packet = header + message

counter_sent = 0
counter_received = 0
total_time = 0
ping_complete = False

while True:
    if button_a.was_pressed():
        message = "ping"
        packet = header + message
        
        while counter_sent < 10: 
            send_time = running_time()
            radio.send(packet)
            display.show(counter_sent)
            counter_sent += 1
    
            # Wait for receiving messages, check what type of message received
            incoming = radio.receive()
            if incoming is not None:
            #Check if message is for me
                if len(incoming) >= 4 and incoming[2:4] == me:
                    # Check if message is pong
                    if(incoming[4:] == "pong"):
                        receive_time = running_time()
                        round_trip_time = receive_time - send_time
                        total_time += round_trip_time
                        counter_received += 1
                        print(round_trip_time)
                    # Check if message is ping
                    elif(incoming[4:] == "ping"):
                        message = "pong"
                        packet = header + message
                        radio.send(packet)
            sleep(1000)
        ping_complete = True
                
    if(ping_complete):
        # Output average RTT  
        if(counter_received > 0):
            average_time = total_time / counter_received
            display.scroll(average_time)
        counter_sent = 0
        counter_received = 0
        total_time = 0
        ping_complete = False