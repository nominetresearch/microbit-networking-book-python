from microbit import *
import radio

radio.on()

my_address = "CS"
their_address = "JG"

# Displays number when received
while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[:2] == their_address:
            data = message[4:]

            # Create empty list when 'Start' is received
            if data == "Start":
                packets_received = []
                sleep(100)
            # When 'End' is received calculate and display packet loss and information loss
            elif data == "End":
                packet_uniques = list(dict.fromkeys(packets_received)) # Removes duplicates from packets_received
                packet_loss = (20 - len(packets_received)) / 20
                information_loss = (10 - len(packet_uniques)) / 10

                display.scroll(str(packet_loss))
                display.show(Image.HEART) # This is just used as a breaker between packet_loss and information_loss
                sleep(1000)
                display.scroll(str(information_loss))
            # Otherwise append to packets_received
            else:
                packets_received.append(data)
                sleep(100)

            message = None