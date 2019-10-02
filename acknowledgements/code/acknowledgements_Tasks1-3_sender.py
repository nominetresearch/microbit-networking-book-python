from microbit import *
import random
import radio

radio.on()

# Sends a string with a % chance of failure
# Returns whether the message was sent succesfully
# Send a message with error
def sendWithError(message, error):
    generated = random.randint(1, 100)
    if generated > error:
        print("Sending:")
        print(running_time())
        radio.send(message)
        return True
    return False

# TASK 1 #
my_address = "JG"
their_address = "CS"
header = my_address + their_address

retransmissions = 0
number = 1
received_ack = False
total_retransmissions = 0

# TASK 2 #
while True:
    # For each message sent, if no reply within 100ms the message is sent again
    # Every retransmission is counted and displayed at the end
    if number < 6:
        #print(str(number))
        packet = header + str(number)
        display.scroll(str(number))

        sendWithError(packet, 50)
        sleep(2000)

        if received_ack:
            received_ack = False
            number += 1
            total_retransmissions += retransmissions
            retransmissions = 0
        else:
            retransmissions += 1

    message = radio.receive()
    if message is not None:
            if message[2:4] == my_address and message[4:] == "ACK":
                print("Recieved ack:")
                print(running_time())
                received_ack = True

    if button_a.was_pressed():
        display.scroll(str(total_retransmissions))

