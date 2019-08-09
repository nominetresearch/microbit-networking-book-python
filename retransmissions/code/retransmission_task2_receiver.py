from microbit import *
import radio

radio.on()

my_address = "CS"
their_address = "JG"

# Displays number when received
while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[:2] == their_address and message[2:4] == my_address:
            data = message[4:]

            # Start counter when 'Start' is received
            if data == "S":
                packets_received = 0
                sleep(100)
            # When 'End' is received calculate and display packet loss
            elif data == "E":
                packet_loss = (10 - packets_received) / 10
                display.scroll(str(packet_loss))
                sleep(1000)
            # Otherwise add 1 to the counter
            else:
                packets_received += 1
                sleep(100)

            message = None