from microbit import *
import radio

# Images for rock, paper, scissors, lizard and spock
rock = Image("00000:09990:09990:09990:00000")
paper = Image("99999:90009:90009:90009:99999")
scissors = Image("99009:99090:00900:99090:99009")
lizard = Image("00900:09990:09990:00900:00090")
spock = Image("09090:09090:09990:09990:09990")

radio.on()

### IMPORTANT ###
# Make sure that on one of the microbits, my_address and their_address are switched around
# if you do not do this you will not be able to play
my_address = "JG"
their_address = "CS"
header = my_address + their_address

selected = False
received = False

# Displays rock by default, pressing A will move to the next image
current_image = "rock"
display.show(rock)
while True:
    # If you haven't confirmed yet, allows you to pick an image using A
    # Pressing B confirms your choice and prevents you from changing yours
    if selected == False:
        if button_a.is_pressed():
            if current_image == "rock":
                display.show(paper)
                current_image = "paper"
            elif current_image == "paper":
                display.show(scissors)
                current_image = "scissors"
            elif current_image == "scissors":
                display.show(lizard)
                current_image = "lizard"
            elif current_image == "lizard":
                display.show(spock)
                current_image = "spock"
            elif current_image == "spock":
                display.show(rock)
                current_image = "rock"
            sleep(500)

        # Once B is pressed, you cannot do anything until your opponent has made their decision
        if button_b.is_pressed():
            my_hand = current_image
            if my_hand == "paper":
                number = 0
            elif my_hand == "rock":
                number = 1
            elif my_hand == "scissors":
                number = 2
            elif my_hand == "lizard":
                number = 3
            elif my_hand == "spock":
                number = 4

            packet = header + str(number)
            radio.send(packet)
            selected = True

    while selected == True:
        # Once you have received your opponents choice, record what it it
        message = radio.receive()
        if message is not None:
            if len(message) == 5 and message[:2] == their_address and message[2:4] == my_address:
                if message[4] == "0":
                    opponent_hand = "paper"
                elif message[4] == "1":
                    opponent_hand = "rock"
                elif message[4] == "2":
                    opponent_hand = "scissors"
                elif message[4] == "3":
                    opponent_hand = "lizard"
                elif message[4] == "4":
                    opponent_hand = "spock"

                message = None
                received = True

        # Displays the appropriate face depending on the outcome
        # After it has been displayed, the game resets for the next round
        #TODO: Reduce the number of elif
        if received == True:
            if my_hand == opponent_hand:
                display.show(Image.SURPRISED)
            elif my_hand == "rock" and (opponent_hand == "scissors" or opponent_hand == "lizard"):
                display.show(Image.HAPPY)
            elif my_hand == "scissors" and (opponent_hand == "paper" or opponent_hand == "lizard"):
                display.show(Image.HAPPY)
            elif my_hand == "paper" and (opponent_hand == "rock" or opponent_hand == "spock"):
                display.show(Image.HAPPY)
            elif my_hand == "lizard" and (opponent_hand == "paper" or opponent_hand == "spock"):
                display.show(Image.HAPPY)
            elif my_hand == "spock" and (opponent_hand == "rock" or opponent_hand == "scissors"):
                display.show(Image.HAPPY)
            else:
                display.show(Image.SAD)

            sleep(3000)
            current_image = "rock"
            display.show(rock)

            selected = False
            received = False