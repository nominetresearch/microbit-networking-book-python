from microbit import *
import radio

# Images for rock, paper and scissors
rock = Image("00000:09990:09990:09990:00000")
paper = Image("99999:90009:90009:90009:99999")
scissors = Image("99009:99090:00900:99090:99009")


radio.on()

# The line below can be used to change the radio group,
# it is already set to 0 by default but can be reconfigured to a number from 0-255
#radio.config(group = 0)

# IMPORTANT 
# Make sure that on one of the microbits, 
# my_address and their_address are switched around
# if you do not do this you will not be able to play
my_address = "JG"
their_address = "CS"
header = my_address + their_address

selected = False
received = False

# Display rock by default, pressing A will 
# move to the next image
current_image = "rock"
my_hand = 1
display.show(rock)
while True:   
    
    # If you have not already selected, 
    # pressing button A allows you to pick an image 
    # Pressing B confirms your choice and prevents you from changing 
    # your selection
    if button_a.was_pressed():
        if not selected:
            if current_image == "rock":
                display.show(paper)
                current_image = "paper"
                my_hand = 0
            elif current_image == "paper":
                display.show(scissors)
                current_image = "scissors"
                my_hand = 2
            elif current_image == "scissors":
                display.show(rock)
                current_image = "rock"
                my_hand = 1
            sleep(500)

    # Once B is pressed, you cannot do anything until your opponent 
    # has made their decision
    if button_b.was_pressed():
        packet = header + str(my_hand)
        radio.send(packet)
        selected = True

    message = radio.receive()
    if message is not None:
        if len(message) == 5 and message[2:4] == my_address:
            opponent_hand = int(message[4])
            message = None
            received = True

    # Displays the appropriate face depending on the outcome
    # After it has been displayed, the game resets for the next round
    if selected and received:
        if my_hand == opponent_hand:
            display.show(Image.SURPRISED)
        elif my_hand == 1 and opponent_hand == 2:
            display.show(Image.HAPPY)
        elif my_hand == 2 and opponent_hand == 0:
            display.show(Image.HAPPY)
        elif my_hand == 0 and opponent_hand == 1:
            display.show(Image.HAPPY)
        else: 
            display.show(Image.SAD)
        selected = False
        received = False
        sleep(1000)   
        current_image = "rock"
        my_hand = 1
        display.show(rock)