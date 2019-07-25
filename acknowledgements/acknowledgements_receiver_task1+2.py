from microbit import *
import radio

radio.on()

### TASK 1 ###
my_address = "CS"
their_address = "JG"
header = my_address + their_address

acknowledge_string = "ACK"
acknowledge_packet = header + acknowledge_string

### TASK 2 ###
data_received = []

# Adds data received to data_received should you wish to access it
# Sends back an acknowledgment after every message received
while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[:2] == their_address:
            data = message[4:]
            if data != "Start" and data != "End":
                data_received.append(data)

            radio.send(acknowledge_packet)
            message = None

            if data == "End":
                for i in data_received:
                    display.show(i)
                    sleep(500)
                    display.show(Image.HEART)
                    sleep(500)
            
