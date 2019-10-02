Reaction Game
==============

This is the game that Jonathan Grout came up with when we worked on this Python edition.
Unlike the rest of the chapters, the Reaction Game is not explained with a step by step guide.
You should use your own knowledge gained from completing the other chapters to 
help you create your program.

The Reaction Game is a simple two-player game inspired by the popular toy *Bop It*[^1]. This game allows you to test your reaction time against a friend by performing actions that the micro:bit tells you to do. On your turn, you'll be asked to complete the action displayed on the micro:bit screen, which will be one of:

- Press button A
- Press button B
- Tilt the micro:bit left
- Tilt the micro:bit right
- Shake the micro:bit

You'll only have a set amount of time to perform the action
and should you get it right, the time you have next turn will decrease so you'll have to be faster. If you run out of time on your turn before you perform the action,
then you lose and your opponent wins. Then the game will switch to your opponent's turn. The radio communication is used to make sure that you and your opponent can coordinate the game turns.

### What you’ll need

    2 micro:bits
    1 teammate

**Description:** You will be programming the reaction game as described above. Make sure to configure your radio to send unicast packets.

**Instructions:** Your program must have these features:

1. A list of actions that the user will try to perform.
2. The game begins when either player presses button A.
3. The game is played in turns, and initially, each player's turn is 3 seconds.
4. On their turn, a player's micro:bit will display a letter ('A', 'B', 'L', 'R' or 'S') corresponding to an action (Press A, press B, tilt left, tilt right or shake).
5. The player must perform that action within their turn duration; otherwise, they lose.
6. If the player completes the correct action, the duration of their next turn will be 250 milliseconds less, down to a minimum of half a second. Then the game switches to opponent's turn.
7. If a player loses, display a sad face on their screen. Display a happy face on the screen of the winner.

### Extended Activity

!!! attention "Exercise 1"
        For a harder version of the game, each player should also lose if they perform the incorrect action on their turn.
        For example, you would lose if the micro:bit displayed 'A', and you pressed button B.
        Modify your code cause a player to lose if they perform the wrong action.


Solutions
---------

Solutions for this chapter can be found in [Github](https://github.com/nominetresearch/microbit-networking-book-python/tree/master/reactiongame/code).

[^1]: Bop It in Wikipedia: [https://en.wikipedia.org/wiki/Bop_It](https://en.wikipedia.org/wiki/Bop_It)

