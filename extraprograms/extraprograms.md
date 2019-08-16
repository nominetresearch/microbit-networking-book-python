Extra Programs
==============

These extra activities are intended as an extension to the other chapters.
Unlike before, these activities will not provide a step by step guide on how to create the program.
You should use your own knowledge gained from completing the other chapters to help you create the program.
These programs can be challenging to code, so if you get stuck try sharing ideas and working together with a friend.
There are two for you to try and program - the Reaction Game and Pong.

The Reaction Game
-----------------

Here is a simple two player game that you can program for the micro:bit inspired by the popular toy *Bop It*[^1].
This game allows you to test your reaction time against a friend by performing
actions that the micro:bit tells you to do.
On your turn you'll be asked to complete the action displayed on the screen, which will be one of:
- Press button A
- Press button B
- Tilt the micro:bit left
- Tilt the micro:bit right
- Shake the micro:bit

You'll only have a set amount of time to perform the action on your turn
and should you get it right, the time you have next turn will decrease so you'll have to be faster.
It will then switch to your opponent's turn.
If you run out of time on your turn before you perform the action,
then you lose and your opponent wins.

### What you’ll need

    2 micro:bits
    1 teammate

**Description:** You will be programming the reaction game as described above. Make sure to configure your
radio to send unicast packets.

**Instructions:** Your program must have these features:
1. A list of actions that the user will try to perform
2. The game will begin when either player presses button A, that player starts the game.
3. Each player will start the game with a turn duration of 3 seconds
4. On their turn, the player's microbit will display a letter ('A', 'B', 'L', 'R' or 'S') corresponding to
an action (Press A, press B, tilt left, tilt right or shake)
5. The player must perform that action within their turn duration, otherwise they lose
6. If the player performs the correct action, the duration of their next turn will be 250 milliseconds less,
down to a minimum of half a second. It will then be their opponents turn.
7. If a player loses, display a sad face on their screen. Display a happy face on the screen of the winner.

### Extended Activity

!!! attention "Exercise 1"
        For a harder version of the game, each player should also lose if they perform the incorrect action on their turn.
        For example, you would lose if the micro:bit displayed 'A' and you pressed button B.
        Modify your code cause a player to lose if they perform the wrong action.

Pong
----

In this activity you will be programming a two-player version of Pong played across two micro:bits.
For those unfamiliar, Pong was one of the first ever videogames created in 1972[^2].
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

### Extended Activity

!!! attention "Exercise 1"
        Discuss with a teammate the effects of changing the length of the paddle to one of length 1, 3, or 4.
        In each case discuss whether you think the game would be more enjoyable or not, and whether you think the length of the program
        would be shorter, the same or longer.

Solutions
---------

Solutions for this chapter can be found under microbit-networking-book-python/extraprograms/code

[^1]: Bop It in Wikipedia: [https://en.wikipedia.org/wiki/Bop_It](https://en.wikipedia.org/wiki/Bop_It)

[^2]: Pong in Wikipedia [https://en.wikipedia.org/wiki/Pong](https://en.wikipedia.org/wiki/Pong)
