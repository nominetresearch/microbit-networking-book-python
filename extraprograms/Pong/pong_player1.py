from microbit import *
import radio
import random

radio.on()

my_address = "JG"
their_address = "CS"
header = my_address + their_address

def updateBatPosition(position):
    # Clear left column
    for i in range(5):
        display.set_pixel(0, i, 0)

    # Display bat pixels
    if position == 1:
        display.set_pixel(0, 0, 9)
        display.set_pixel(0, 1, 9)
    elif position == 2:
        display.set_pixel(0, 1, 9)
        display.set_pixel(0, 2, 9)
    elif position == 3:
        display.set_pixel(0, 2, 9)
        display.set_pixel(0, 3, 9)
    else:
        display.set_pixel(0, 3, 9)
        display.set_pixel(0, 4, 9)

def updateBallPosition(x, y, up, right):
    # Remove ball
    display.set_pixel(x, y, 0)

    # Move ball to new position
    if y == 0 and up == True:
        y += 1
        up = False
    elif y == 4 and up == False:
        y -= 1
        up = True
    elif up == True:
        y -= 1
    else:
        y += 1
 
    if right == True:
        x += 1
    else:
        x -= 1

    display.set_pixel(x, y, 9)
    return [up, right]


bat_position = 2
updateBatPosition(bat_position)

# Player 1 serves first
my_side = True

# Ball begins in defined position
ball_x = 4
ball_y = 3
up = False
right = False
display.set_pixel(ball_x, ball_y, 9)

# Scores
my_score = 0
opponent_score = 0

start = False

while True:
    # If start is false, wait for player to press A to begin
    while start == False:
        if button_a.is_pressed():
            start = True
            sleep(500)

    # Move bat up if A is pressed
    if button_a.is_pressed():
        if bat_position != 1:
            bat_position -= 1
            updateBatPosition(bat_position)
    
    # Move bat down if B is pressed
    elif button_b.is_pressed():
        if bat_position != 4:
            bat_position += 1
            updateBatPosition(bat_position)

    if my_side == True: # If the ball is on this side

        # If the ball is at the edge, opponent gets a point
        if ball_x == 0:
            radio.send(header + "P")
            opponent_score += 1
            display.clear()

            # Opponent wins if they score 5
            if opponent_score == 5:
                while True:
                    display.show(Image.SAD)

            # Display my score for 2 seconds
            display.show(str(my_score))
            sleep(2000)
            display.clear()
            updateBatPosition(bat_position)

            # Reset ball for new serve
            ball_x = 4
            ball_y = random.randint(0, 4)
            if ball_y == 0:
                up = False
            elif ball_y == 4:
                up = True
            else:
                up = random.choice([True, False])
            display.set_pixel(ball_x, ball_y, 9)

            right = False
            start = False
        
        else:
            # Checks if the incoming ball has hit the bat or not
            if ball_x == 1 and right == False:
                if ball_y == 0:
                    if bat_position == 1:
                        right = True
                elif ball_y == 1:
                    if bat_position == 1 or bat_position == 2:
                        right = True
                elif ball_y == 2:
                    if bat_position == 2 or bat_position == 3:
                        right = True
                elif ball_y == 3:
                    if bat_position == 3 or bat_position == 4:
                        right = True
                elif ball_y == 4:
                    if bat_position == 4:
                        right = True

            # Updates the position of the ball each cycle if the ball is on this microbit
            if ball_x < 4 or right == False:
                updates = updateBallPosition(ball_x, ball_y, up, right)
                if updates[0] == True:
                    up = True
                    ball_y -= 1
                else:
                    up = False
                    ball_y += 1

                if updates[1] == True:
                    right = True
                    ball_x += 1
                else:
                    right = False
                    ball_x -= 1
            # Send ball to opponent if ball is going off screen
            else:
                display.set_pixel(ball_x, ball_y, 0)
                if ball_y == 0 and up == True:
                    ball_y += 1
                    up = False
                elif ball_y == 4 and up == False:
                    ball_y -= 1
                    up = True
                elif up == True:
                    ball_y -= 1
                else:
                    ball_y += 1

                if up == True:
                    up_str = "U"
                else:
                    up_str = "D"
                radio.send(header + "B" + up_str + str(ball_y)) # Sends ball position and whether it is moving up or down
                my_side = False

    else: # If the ball isn't on this side
        message = radio.receive()
        if message is not None:
            # If ball is received, then display and switch
            if message[:2] == their_address and message[4] == "B":
                if message[5] == "U":
                    up = True
                else:
                    up = False
                right = False
                ball_y = int(message[6])
                ball_x = 4
                display.set_pixel(ball_x, ball_y, 9)

                my_side = True
            
            # Gain a point if opponent missed the ball
            elif message[:2] == their_address and message[4] == "P":
                my_score += 1
                display.clear()

                # Win if score is 5
                if my_score == 5:
                    while True:
                        display.show(Image.HAPPY)

                display.show(str(my_score))
                sleep(2000)
                display.clear()
                updateBatPosition(bat_position)

    sleep(250) # This is the update time, every 250ms the ball and the bat move
