from microbit import *
import radio
import random

radio.on()

my_address = "JG"
their_address = "CS"
header = my_address + their_address

# 'A' - press button A
# 'B' - press button B
# 'L' - tilt left
# 'R' - tilt right
# 'S' - shake
movements = ['A', 'B', 'L', 'R', 'S']

# Checks if the user performed the required action in time
def timedGesture(gesture, time_remaining):
    passed = False
    while not passed and time_remaining > 0:
        if gesture == 'A':
            if button_a.is_pressed():
                passed = True
        elif gesture == 'B':
            if button_b.is_pressed():
                passed = True
        elif gesture == 'L':
            if accelerometer.was_gesture("left"):
                passed = True
        elif gesture == 'R':
            if accelerometer.was_gesture("right"):
                passed = True
        else:
            if accelerometer.was_gesture("shake"):
                passed = True
        time_remaining -= 5
        sleep(5)
    return passed

# Pressing A begins game, that player will go first
my_turn = False
start = False
game_in_progress = False

# Time each turn
time_remaining = 3000

# Begin game
while True:
    message = radio.receive()
    if message is not None:
        if message[2:4] == my_address:
            if message[4:] == "START":
                start = True
                radio.send(header+"ACK")
            elif message[4:] == "ACK":
                start = True
                my_turn = True
            elif message[4:] == "SWITCH":
                my_turn = True
            elif message[4:] == "LOSE":
                display.show(Image.HAPPY)
                sleep(2000)
                game_in_progress = False
                display.clear()
                
    if button_a.was_pressed():
        if not game_in_progress: 
            radio.send(header + "START")

    if start:
        # Countdown
        display.show("3")
        sleep(1000)
        display.show("2")
        sleep(1000)
        display.show("1")
        sleep(1000)
        display.clear()
        start = False
        game_in_progress = True

    if game_in_progress and my_turn:
        gesture = random.choice(movements)  # Picks random gesture
        display.show(gesture)

        succeeded = timedGesture(gesture, time_remaining)
        if not succeeded:  # Fail the gesture -> lose the game
            radio.send(header + "LOSE")
            display.show(Image.SAD)
            sleep(2000)
            game_in_progress = False
        else:  # Otherwise switch turns
            radio.send(header + "SWITCH")
        display.clear()
        if time_remaining > 250:  # Lowers maximum time
            time_remaining -= 250
        my_turn = False