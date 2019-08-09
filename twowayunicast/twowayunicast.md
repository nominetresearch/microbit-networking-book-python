Two-way unicast
===============

![Chapter 6 image](chapter6.png)

Introduction
------------

In this chapter, you will learn about *bidirectional communication*:
sending a message to another micro:bit and getting a response to
your message. You will also learn about the Ping program, which is a
commonly used tool to check if computers are still connected to the
internet.

This chapter will build on the learnings from the previous chapter,
[Unicast Communication: One to One](../unicast/unicast.md). The new ideas are:

- The idea of 2-way communication (*bidirectional communication*)

- The Ping program

- The concept of round-trip-time

### What you’ll need

    2 micro:bits
    1 whiteboard/board
    Boardmarkers/postit notes
    1 teammate

Background
----------

*Bidirectional communication* enables two-way communication between two
computers.

!!! hint "Definition 1: _Bidirectional communication_"
	This is a communications mode in which
	data is transmitted in both directions but not at the same time.

In the previous chapter, your micro:bits had clear roles: there was a
sender and a receiver. In bidirectional communication, either of the
micro:bits can send and receive messages. This way, it becomes possible
to create two-way protocols. In these protocols, when a computer sends a
message, it waits for a certain response to its message.

!!! hint "Definition 2: _Ping_"
	Ping is an example of a two-way protocol. It is widely used in
	the internet to test whether a networked computer is connected OK.

Ping program sends a *Ping* message and
expects this message to be echoed back, for example with a *Pong*
message. This is like playing ping pong but with computers and over
networks. If the sender does not receive a response to its *Ping*, this
shows there is a problem with the receiver.

It is also a problem if it
takes a long time before the sender receives a *Pong* response.
To spot these problems, the Ping program measures the *round-trip-time* between the two
computers.

!!! hint "Definition 3: _Round-trip-time (RTT)_"
	Round-trip-time is the time it takes for a
	message to go from a sender to a receiver and back again.

In other words, the sender measures the difference in time when it sent
the *Ping* and when it received the *Pong*.  

RTT = Time\_receive\_pong - Time\_send\_ping  

The figure below shows the relationship between,
*Ping*, *Pong*, and round-trip-time.

![Round-trip-time. Micro:bit 1 sends a *Ping* message to Micro:bit 2 at *Time\_send*. The Micro:bit 2 responds with a *Pong* message. Micro:bit 1 receives the *Pong* message at *Time\_receive*. The difference between these two times, *Time\_receive* and *Time\_send* is the round-trip-time.](Ping-rtt.png)

!!! note ""
	**Figure 1:** Round-trip-time. Micro:bit 1 sends a *Ping* message to 
	Micro:bit 2 at *Time\_send*. The Micro:bit 2 responds with a *Pong* message. 
	Micro:bit 1 receives the *Pong* message at *Time\_receive*. The difference 
	between these two times, *Time\_receive* and *Time\_send* is the round-trip-time.

Besides round-trip-time (RTT), the Ping program reports statistical
information. The figure below shows an example output as a result of
using the command:

    ping www.google.com

on the <http://ping.eu/ping> website. In this example, four Ping messages were sent to *www.google.com*.
The round-trip-time for each message is given with the *time* value in
each line. For example, for the first ping, the RTT is 10.2 ms
(milliseconds). The program also reports ping statistics. For example, 4
packets were sent, 4 packets were received. This means 0% packet loss.
The average RTT (shown as *avg*) is 10.184 ms.

![The output of running ping to send four messages to *www.google.com*. The <http://ping.eu/ping> online program reports round-trip time and a statistical summary of the results.](PingGoogle.png)

!!! note ""
	**Figure 2:** The output of running ping to send four messages to *www.google.com*. 
	The <http://ping.eu/ping> online program reports round-trip time and a 
	statistical summary of the results.

When programming your micro:bit, you
will use the `running_time()` function to calculate the round-trip-time of your messages. This function returns the number of milliseconds since the micro:bit was last switched on. To calculate the round-trip time, you will need to record the time
when you first sent a message, and also when you received a response.

Programming: Ping
-----------------

This activity is best done with a team of two. To program the Ping program, you will need to complete five tasks.

### Task 1: Prepare for unicast

**Description:** Ping uses unicast between the sender and the receiver
micro:bits. Look at your notes for the previous chapter, [Unicast Communication: One to One](../unicast/unicast.md)  and your
unicast program to remember how to do unicast.

**Instruction:** Start with using the unicast program you have written for
[Unicast Communication: One to One](../unicast/unicast.md) as a basis. In this program, decide which
micro:bit is going send the *Pings*, and which micro:bit is going to
respond with *Pongs*. Set the address variables based on your decision.
Design your message header, *Ping* packet, and *Pong* packet.

### Task 2: Send a Ping

**Description:** The ping sender records the time before it sends out a
*Ping* packet. It unicasts the *Ping* packet.

**Instruction:** Use `running_time()` to record the *Ping* sending time.
Send a *Ping* packet to the receiver micro:bit.

### Task 3: Receive a Ping

**Description:** The receiver micro:bit responds a *Ping* message with a
*Pong*.

**Instruction:** Program the receiver micro:bit to unicast a *Pong*
packet when a *Ping* packet is received.

### Task 4: Receive a Pong and calculate round-trip-time

**Description:** When the sender micro:bit receives the *Pong*, it
calculates the round-trip-time.

**Instruction:** Program the sender to
receive a *Pong* packet. When the *Pong* is received, record the time
using `running_time()` function. Show the difference between receiving
and sending times on your display. 

### Task 5: Put everything together
**Description:** Combine all the code you have written from Task 1 to Task 4, so that a single micro:bit can run the Ping program both as a Ping sender and a receiver.

**Instruction:** Use one of your micro:bits to send a Ping 5 times, and write down the round-trip-times that you see in your display. Answer these two
questions:

1. What is the minimum and maximum round-trip-time (RTT)?

2. What is the average RTT?

Exercises
---------

!!! attention "Exercise 1"
	Extend your Ping program to send automatically more than one *Ping* message.
	Test it with 10 *Pings*. Calculate the average round-trip time of these Ping messages.

!!! attention "Exercise 2"
	The Ping program reports the round-trip-time. What if you wanted to calculate 
	the time the message took one way? Is it possible to calculate one-way times? 
	In other words, is it possible to calculate how long it takes to send a message 
	from the sender to the receiver? How long the messages take from the receiver to the sender?

Problems
--------

1. In the example ping figure from the <http://ping.eu/ping> site, what is 172.217.23.228?

2. What is round-trip-time, and how is it calculated?

3. Think about the following scenario: micro:bit 1 sends a *Ping* to micro:bit 2 at time *5*. If the round-trip-time is *10*, at what time did the micro:bit 1 receive the *Pong* message?

4. In the example ping figure from the <http://ping.eu/ping> site, what are the minimum and maximum round-trip-times (RTTs)?

5. In the example ping figure from the <http://ping.eu/ping> site, the packet loss 0% loss. What is the loss percentage, if 2 *Ping* messages were lost out of 5?

Resources
---------

Video: What is a Ping? - <https://youtu.be/N8uT7LNVJv4>
