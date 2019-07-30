from microbit import *
import random
import radio

radio.on()

# Sends a string with a % chance of failure
# Returns whether the message was sent succesfully
def sendStringWithError(string, chance):
    generated = random.randint(1,100)
    if generated <= chance:
        sent = True
    else:
        sent = False

    if sent == False:
        radio.send(string)

    return sent

### TASK 2 ###
# Every 5ms checks to see if an acknowledgment message has been recieved, up to 'time' ms
# Will return True if acknowledged or False if not
def ackWait(time):
    received = False
    time_passed = 0
    while time_passed <= time and received == False:
        message = radio.receive()
        if message is None:
            time_passed += 5
            sleep(5)
        else:
            if message[4:] == "ACK":
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

        for digit in range(1, 6):
            packet = header + str(digit)
            while True:
                sendStringWithError(packet, 50)
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

