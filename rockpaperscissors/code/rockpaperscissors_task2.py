from microbit import *
import radio

# Images for rock, paper and scissors
rock = Image("00000:09990:09990:09990:00000")
paper = Image("99999:90009:90009:90009:99999")
scissors = Image("99009:99090:00900:99090:99009")

radio.on()

### IMPORTANT ###
# Make sure that on one of the microbits, my_address and their_address are switched around
# if you do not do this you will not be able to play
my_address = "JG"
their_address = "CS"
header = my_address + their_address

# Displays rock by default, pressing A will move to the next image
current_image = "rock"
display.show(rock)
while True:
    if button_a.is_pressed():
        if current_image == "rock":
            display.show(paper)
            current_image = "paper"
        elif current_image == "paper":
            display.show(scissors)
            current_image = "scissors"
        elif current_image == "scissors":
            display.show(rock)
            current_image = "rock"
        sleep(500)

    # Pressing B sends your choice to the other microbit
    if button_b.is_pressed():
        choice = current_image
        if choice == "paper":
            number = 0
        elif choice == "rock":
            number = 1
        elif choice == "scissors":
            number = 2

        packet = header + str(number)
        radio.send(packet)

    # Displays your opponents choice when their message has been received
    message = radio.receive()
    if message is not None:
        if len(message) == 5 and message[:2] == their_address:
            if message[4] == "0":
                display.show(paper)
            elif message[4] == "1":
                display.show(rock)
            elif message[4] == "2":
                display.show(scissors)

            message = None