Extra Activities: Pong
=====================

Introduction
------------
In this activity you will be programming a two-player version of Pong played across two micro:bits.
For those unfamiliar, Pong was one of the first ever videogames created in 1972[^1].
It is a two-dimensional simulation of table tennis featuring two paddles (bats),
a ball which bounces off the sides of the screen, a net in the centre and a score which is displayed
on screen for each player.

Due to the micro:bit's limited screen size and memory, your version will not have as many features as the original.
For instance, as this version will be played across two micro:bits, there will be no net. 
Instead the net will be represented by the space between the two micro:bits.
In addition, the score will only be displayed after each round and the ball
will always bounce at an angle of the same magnitude (45 degrees up from the horizontal
or 45 degrees down from the horizontal)
The paddle will be two pixels long and the ball will be one pixel.
To win the game you will need to score 5 points.

You can choose whether you want to have the paddles on the left of one micro:bit and on the right of the other 
so that you'd play sitting next to each other.
Or you can have the paddles on the bottom of the screen so that you'd play sitting opposite each other.
Each version will play identically but will require different code.

### What you’ll need

    2 micro:bits
    1 teammate

Programming: Playing Pong
----------------------------------

**Description:** You will be programming Pong as described above. Make sure to configure your
radio to send unicast packets. 
Experiment with different update delays to find one that allows the program to be played fairly.

**Instructions:** Your program must have these features:
1. The program must use LEDs to show the positions of the paddles and the ball. The program will update
the screen as quick as it can which is too fast to see, so add an update delay (sleep) to slow the program down
2. Pressing A will move your paddle up/left, pressing B will move your paddle down/right
3. At the start of the game or at the start of each round, pressing A will serve the ball to your opponent
4. Choose a player to serve at the start of the game, from then on the loser of each round will serve next
5. Pressing A will serve the ball and start the round
6. The ball moves at 45-degree angles, so the program must know whether the ball is moving up or down and left or right
7. If the ball collides with a paddle, rebound in the opposite direction.
8. If the ball collides with the edges of the screen (perpendicular to where the paddles move), rebound in the opposite direction
9. If a player fails to hit the ball with their paddle before it reaches the edge of their screen (parallel to where the bats move),
their opponent will gain a point. This ends the round.
10. At the end of each round, clear the screen and display the score for two seconds. Then display the game again.
11. When a player reaches 5 points, display a happy face on their screen and a sad face on their opponents.

Extended Activity
-----------------

!!! attention "Exercise 1"
        Discuss with a teammate the effects of changing the length of the paddle to one of length 1, 3, or 4.
        In each case discuss whether you think the game would be more enjoyable or not, and whether you think the length of the program
        would be shorter, the same or longer.

[^1]: Pong in Wikipedia [https://en.wikipedia.org/wiki/Pong](https://en.wikipedia.org/wiki/Pong)