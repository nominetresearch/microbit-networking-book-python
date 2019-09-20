Handling Errors: Retransmissions
================================

![Chapter 8 image](chapter8.png)

Introduction
------------

In the previous chapters, you probably noticed wireless communication isn’t always
reliable. In other words, not every message you send may be received on
the other side. In this chapter, you will learn about how to improve your chances.
One simple but effective method is using retransmissions.

In this chapter, you will learn about:

- Wireless communication errors

- *Retransmissions* as a method of improving reliability.

### What you’ll need

    2 micro:bits
    1 teammate

Background
----------

In wireless communications, an error can occur for several reasons.
For example, there may be physical obstructions, like walls, doors, and
even people. The wireless signals lose power as they go through these
obstructions and sometimes,  bounce off them.
The more obstructions there
are between a sender and a receiver, the more chance there is of an
error. Also, if the sender and receiver are too far away from each
other, they may not always be able to communicate. Imagine there are
many obstacles between two people, they may not always hear what the
other one is saying.

Another reason for a wireless error may be *radio interference*. This is
because wireless communication is broadcast (remember
[Wireless and Broadcast Communication](../broadcast/broadcast.md)). This means that there may be many
broadcasters, and their transmissions may collide at the receivers.
These broadcasters *interfere* with each other.

!!! hint "Definition 1: _Interference_"
	In wireless communications, interference is any other
	signal that disrupts a signal as it travels to its destination.

Imagine, in a classroom, when everybody is talking at the same time. You
will miss half of the things your friend says. Other people’s signals
interfere with your friend’s signal on its way to you. In networking,
this is a packet loss.

!!! hint "Definition 2: _Packet loss_"
	Packet loss happens when one or more data packets
	traveling in a computer network do not reach their destination. Packet
	loss is measured as the ratio of packets lost and the packets sent (see
	Equation below).

*Packet loss* = (*Packets lost*)/(*Packets sent*)

Also, if there is too much interference, you may receive messages
incorrectly. For instance, you may hear “Bat!” when your friend is
shouting “Cat!”. In networking, this is a packet error. Packet errors are measured as packet error rates.

!!! hint "Definition 3: _Packet error rate_"
	Packet error rate is the ratio of packets that have been received with
	one or more errors and the packets sent.

*Packet error rate* = (*Packets with errors*)(*Packets sent*)

In this chapter, we will cover one simple method to handle these errors, *retransmissions*, where the sender automatically retransmits messages multiple times to increase the
chance of reception.

!!! hint "Definition 4: _Retransmissions_"
	Retransmissions mean sending messages many times.

In the figure below, let’s assume the sender knows that
the communications medium loses half of its packets. In other words, the
packet loss is 0.5 (or 50%). The sender micro:bit decides to send each packet twice to
increase the chance to get its messages through. The first packet is the
transmission, and the second packet is the retransmission. So, the
number of retransmissions is 1.

![Retransmissions may increase message success. In the example, the sender sends each message twice by default. So, even if the first “Hello” failed, the second “Hello” was received by the receiver.](Retransmissions.png)

!!! note ""
	**Figure 1:** Retransmissions may increase message success.
	In the example, the sender sends each message twice by default. So, even if 
	the first “Hello” failed, the second “Hello” was received by the receiver.

It is common to use retransmissions combined with another method. For
instance, senders may choose to retransmit only when they are sure there
has been an error. We will explore this option in the next chapter,
[Handling errors: Acknowledgements](../acknowledgements/acknowledgements.md).

Programming: Retransmissions
----------------------------

This activity is best done with a teammate. You will start with creating
packet errors in Task 1, and then test different packet error rates in
Task 2. In Task 3, you will program the retransmissions solution to
handle these errors. In this task, you will also run a series of
experiments to measure how well retransmissions works.

### Task1: Create packet errors

**Description:** In wireless communication, packets may fail randomly.
This may make testing your code for this chapter difficult. To test
errors, you will create a function to send messages with errors.

```Python
import radio
import random

def sendWithError(message, error):
    generated = random.randint(1, 100)
    if generated > error:
        radio.send(message)
        return True
    return False
```

This function takes two arguments: 'message' and 'error' value between 1-100.
Then, it generates a random number, and compares it with 'error'.
Only if the random value is larger than 'error', the message is sent.
The function returns True if the message was sent and False, otherwise.

**Instruction** Copy the code above into your own program.
With your teammate, decide who will have the sender micro:bit, and who will have the
receiver micro:bit. Follow the approach in [Unicast Communication: One to One](../unicast/unicast.md)
to put sender and receiver addresses in your packets.
You may copy and
change one of the programs you have written for
[Unicast Communication: One to One](../unicast/unicast.md).

Write a small sender program that sends a number with an error. Write a small receiver program that receives a
number and displays it on screen.

Experiment with these programs by changing the packet error rate using these error values in your program:
0, 50 and 100. Test packet errors by observing the receiver display.

### Task 2: Send a sequence of messages

**Description:** In this section, you will send a sequence of messages
to the receiver micro:bit.

**Instruction:** Extend your program in Task 1, to send this sequence:

    S 1 2 3 4 5 6 7 8 9 10 E

In this sequence, 'S' signals the start of the sequence, and 'E' signals the end of the sequence.
You can send the 'S' and 'E' using the normal *radio.send()* function to
send them without an error. But remember that your micro:bit’s radio may
drop messages. So, there may be errors even in sending 'S' and 'E'. No radio is perfect!

Extend the receiver program to count the number of messages it receives
in this sequence. Run experiments setting the *error* parameter to 25,
50, and 75. Calculate the packet loss using the Packet loss equation. Repeat each experiment three times. Fill
the table below with the result of your experiments. For
example, when *error* is set to 25 in experiment number 1, if you
received:

    S 1 5 6 7 8 9 10 E

This means, you received 7 packets, and lost 3. Your packet loss is 30% (0.3). The first row of the table is filled based on this example. Add in the values from your own experiment based on your experiment results. Discuss with your teammate how the experiment results change as you change the value  of the *error* variable.

| **Error value** | **Experiment no.** | **Packets received**| **Packet loss** |
|-----------------|:-------------------|:---------------|:-----------------|
| 25 | (Example) | 7| 0.3
| 25 | 1 | | |
| 25 | 2 | | |
| 25 | 3 | | |
| 50 | 1 | | |
| 50 | 2 | | |
| 50 | 3 | | |
| 75 | 1 | | |
| 75 | 2 | | |
| 75 | 3 | | |

Task 3: Retransmit by default
-----------------------------

**Description:** In this task, you will program the automatic
retransmissions at the sender side.

**Instructions:** Change your sender code from Task 2 to send each
number in your sequence more than once. To try out your code, set
*error* to 75. For example, by setting number of retransmissions to 1,
you will send the following sequence:

    S 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 E

This means the sender sent 20 packets in total, including 10
retransmissions.

Change your receiver code to count the unique numbers received.  Count
also the duplicates. Calculate the packet loss. For example,
let’s assume your receiver received, for the case of 1 retransmission:

    S 1 1 2 3 5 5 6 8 9 9 10 E

This means, the receiver received 8 unique numbers (1, 2, 3, 5, 6, 8, 9 and 10) and 3 duplicates (1, 5 and 9). Note that the packet loss is 9 packets out of 20 (45%). But with retransmissions, the receiver only lost 2
numbers out of 9 (it did not receive 4 and 7). Let’s call this improved
packet loss, the *information loss*. So, the information loss with
retransmissions is 2/10 or 0.2. The first row of the table below is filled based on this example.

Run each experiment three times each, for different retransmission values and fill in the rest of the table.

| **Retransmissions** | **Experiment** | **Unique Packets Received**| **Duplicates** |**Packet loss** | **Information loss**|
|---------------------|:---------------|:----------------|:--------------------|-----------------|:----------------|
| 1 | (example) | 8 | 3 | 0.45 | 0.2|
| 1 | 1 |  | | | |
| 1 | 2 |  | | | |
| 1 | 3 |  | | | |
| 3 | 1 |  | | | |
| 3 | 2 |  | | | |
| 3 | 3 |  | | | |
| 5 | 1 |  | | | |
| 5 | 2 |  | | | |
| 5 | 3 |  | | | |

Extended activity
-----------------

!!! attention "Exercise 1"
	Based on your experiments, discuss with your teammate how the increase in 
	retransmissions helps. In your discussion, answer the following questions:
	
	- How does the information loss improve as you increase the number of retransmissions?
	- Does the method guarantee all messages are received at least once?
	- How would you improve your method?

!!! attention "Exercise 2"
	Imagine you are going to survey packet loss in different locations inside a room using two micro:bits. Write a receiver and a sender program to measure packet loss. What do you observe? How does the packet loss change in different locations?

Problems
--------

1. What is interference? Why does it happen?

2. If the sender sent 20 messages, and 11 messages were lost on the way to the destination, what is the packet loss?

3. If the packet error rate is 20% and the sender sent 40 packets, how many packets had errors?

4. Assume you do not know how many numbers that will be in the message sequence. But, you know the numbers will start from 1, and will increment by 1. For example, the sent message sequence may be: *S 1 2 3 4 5 6 7 8 9 10 11 12 E*. What happens if you lose the 'S' or 'E'? Which one is worse: the loss of the 'S' or the 'E' message? If the only message you receive is a 4, what can you say about the number of messages you lost?

5. Assume you do not know how many numbers that will be in the message sequence. And they do not follow any order. For example, the sent message sequence may be: *S 3 5 10 2 E*. What happens if you lose 'S' or 'E' messages in the sequence. Which one is worse: the loss of 'S' or 'E' message? If the only message you receive is a 5, what can you say about the number of messages you lost?

Solutions
---------

Solutions for this chapter can be found under [the GitHub Directory](/code).
You can find example test results in [ExampleTestResults.md](ExampleTestResults.md).

Resources
---------

Video: The Internet: Packet, Routing and Reliability -
    <https://youtu.be/AYdF7b3nMto>
