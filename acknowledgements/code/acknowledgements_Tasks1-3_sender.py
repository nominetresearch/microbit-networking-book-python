from microbit import *
import random
import radio
import utime

radio.on()

# Sends a string with a % chance of failure
# Returns whether the message was sent succesfully
# Send a message with error
def sendWithError(message, error):
    generated = random.randint(1, 100)
    if generated > error:
        radio.send(message)
        return True
    return False


### TASK 2 ###
# Checks to see if an acknowledgment message has been recieved, up to 'time' ms
# Will return True if acknowledged or False if not
def ackWait(time):
    received = False
    start_time = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start_time) <= time and received == False:
        message = radio.receive()
        if message is not None:
            if message[:2] == their_address and message[2:4] == my_address and message[4:] == "ACK":
                received = True
    return received

### TASK 1 ###
my_address = "JG"
their_address = "CS"
header = my_address + their_address

### TASK 2 ###
while True:
    # For each message sent, if no reply within 100ms the message is sent again
    # Every retransmission is counted and displayed at the end
    retransmissions = 0
    if button_a.is_pressed():
        while True:
            radio.send(header + "Start")
            response = ackWait(100)
            if response == True:
                break
            else:
                retransmissions += 1

        for number in range(1, 6):
            packet = header + str(number)
            while True:
                sendWithError(packet, 50)
                response = ackWait(100)
                if response == True:
                    break
                else:
                    retransmissions += 1

        while True:
            radio.send(header + "End")
            response = ackWait(100)
            if response == True:
                break
            else:
                retransmissions += 1

        display.scroll(str(retransmissions))

