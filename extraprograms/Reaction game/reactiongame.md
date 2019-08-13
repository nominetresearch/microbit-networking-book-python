Extra Activities: The Reaction Game
=====================

![Reaction game image](chapter4.png)

Preface
-------
These extra activities are intended as an extension to the other chapters.
Unlike before, these activities will not provide a step by step guide on how to create the program.
You should use your own knowledge gained from completing the other chapters to help you create the program.
These programs can be challenging to code, so if you get stuck try sharing ideas and working together with a friend.

Introduction
------------
Here is a simple two player game that you can program for the micro:bit.
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

Programming: Playing The Reaction Game
----------------------------------

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

Extended Activity
-----------------

!!! attention "Exercise 1"
        For a harder version of the game, each player should also lose if they perform the incorrect action on their turn.
        For example, you would lose if the micro:bit displayed 'A' and you pressed button B.
        Modify your code cause a player to lose if they perform the wrong action.
