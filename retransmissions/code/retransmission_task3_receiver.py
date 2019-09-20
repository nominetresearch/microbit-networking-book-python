from microbit import *
import radio

radio.on()

my_address = "CS"
their_address = "JG"

# Displays number when received
while True:
    message = radio.receive()
    if message is not None:
        if len(message) >= 5 and message[2:4] == my_address:
            data = message[4:]

            # Create empty list when 'S' is received
            if data == "S":
                packets_received = []
                for i in range(1, 12):
                    packets_received.append(0)
                sleep(100)
            # When 'E' is received
            # calculate and display packet loss and information loss
            elif data == "E":
                total_received = 0
                information_received = 0
                for i in range(1, 11):
                    if(packets_received[i] > 0):
                        information_received += 1
                    total_received += packets_received[i]
                packet_loss = (20 - total_received) / 20
                information_loss = (10 - information_received) / 10
                display.scroll(str(packet_loss))
                display.show(Image.HEART)
                sleep(1000)
                display.scroll(str(information_loss))
            # Otherwise append to packets_received
            else:
                print(data)
                packets_received[int(data)] += 1
                sleep(100)
            message = None