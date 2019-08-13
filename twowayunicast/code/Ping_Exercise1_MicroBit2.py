from microbit import *
import radio

# Turn radio on 
radio.on()

# Create the header
string_sender = "PO"
string_receiver = "PI"
header = string_sender + string_receiver

# Create the message and attach to header to form package
message = "ping"
packet = header + message

counter = 0
total_time = 0

while True:
    if button_a.is_pressed():
        # Calculate the RTT 10 times
        while counter < 10:
            # Send message
            send_time = running_time()
            message = "ping"
            packet = header + message
            radio.send(packet)

            # When a message is received, calculate and display the round trip time
            received = False
            while received == False:
                incoming = radio.receive()
                if incoming is not None:
                    if len(incoming) >= 4 and incoming[:2] == string_receiver and incoming[2:4] == string_sender:
                        received = True
            
            receive_time = running_time()
            round_trip_time = receive_time - send_time
            total_time += round_trip_time

            incoming = ""
            counter += 1

        # Output average RTT                 
        average_time = total_time / 10
        display.scroll(average_time)
        counter = 0
        total_time = 0
            
    else:
        # Checks for messages, any of length 4 or greater will be kept
        incoming = radio.receive()
        if incoming is not None:
            if len(incoming) >= 4 and incoming[:2] == string_receiver and incoming[2:4] == string_sender:
                message = "pong"
                packet = header + message
                radio.send(packet)

                incoming = ""