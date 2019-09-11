Unicast communication: One to One
=================================

![Chapter 5 image](chapter5.png)

Introduction
------------

Unicast, sending messages to a single receiver, is how we typically communicate on the Internet. For example, to view a web page, we send messages to a server, which in turn sends us the page to display on our browser.

In this chapter, you will send unicast messages, for example to a
friend’s or teammate’s micro:bit. Doing this, you will learn some core ideas of computer networking, including:

- the concept of *unicast*

- the concept of a *protocol*

- the concept of an *address* and *IP address*

- the concept of a *data packet* and a *header*

### What you’ll need

    2 micro:bits
    1 whiteboard/board
    Boardmarkers/post-it notes
    1 teammate

Background
----------

This chapter covers unicast communication. So, what is unicast?

!!! hint "Definition 1: _Unicast_"
	Transmission of a message to a single receiver.

To understand how we can enable unicast, we will first
look at how computers transmit messages to each other using *protocols*.

!!! hint "Definition 2: _Protocol_"
	A set of rules for how messages are sent across networks.

Simply, protocols define how computers should send messages and what
they should do when they receive a message. So, we can use a protocol to say who the message is for.

This is exactly what is happening on the internet, where every
computer or device follows the Internet Protocol (IP).
According to Internet Protocol, each device is given a unique *address*, called an *IP address*. 

!!! hint "Definition 3: _IP address_"
	A unique string that identifies computers that use the
	Internet Protocol  to communicate over a network. This string is made up of 4 decimal numbers, that range between 0 and 255. Each decimal is separated by dots. For example, 213.248.234.11 is an IP address.

Remember, in the previous chapters, you changed your micro:bit's group ID in your programs to broadcast or multicast.  Setting the group ID helped you to limit the group of micro:bits to receive messages from each other. If the group is limited to two micro:bits, then this enables unicast communication between them.

But, what if we want each micro:bit to have its address (like the IP address) that we can send messages directly too. Note that, in this case, two micro:bits should have the same group ID to be able to  send to and receive messages from each other.

To support an address for each micro:bit, we can modify what we send so that it also includes who the message is for.  On the internet, when two computers communicate, the sender sends a data packet, which includes both the message and address information.

!!! hint "Definition 4: _Data packet_" 
	A data packet is a piece of data sent over a network.
	This piece of data has an actual message part (for example, an image or a text) and one or more header parts. A header contains helpful information for protocols like the sender and receiver IP addresses.

![A data packet contains a message and a header. A header contains information to help a protocol such as sender and receiver addresses, and message types. Different protocols may add different headers to a message.](Datapacket.png)

!!! note ""
	**Figure 1:** A data packet contains a message and a header. A header contains information to help a protocol such as sender and receiver addresses, and message types. Different protocols may add different headers to a message.

The figure above shows how the data and one header forms a data
packet. In this figure, as well as the sender and receiver addresses, the example header also includes a message type. Message type tells the receiver what type of a message it is receiving, for example, whether it is a text or an image. This helps the receiver micro:bit to decide how to process, for example, display the message.

In this chapter, to unicast to other micro:bits, you will create a data packet by adding a header with source and destination addresses.

Programming: Sending and receiving unicast messages
---------------------------------------------------

To program unicast communication, you will need to complete four tasks. To start with, you need two micro:bits.

For unicast to work, micro:bits should receive all messages sent, but the program should read only the ones that are addressed to the intended receiver. This is like seeing all the post coming into your house, but only opening the envelopes with your name on.

### Task 1: Configure your radio

**Description:** To receive any packet, sent by anybody, you need to use broadcast as the underlying communication.

**Instruction:** Set your radio group ID like you did in [Broadcast Communication: One to All](../broadcast/broadcast.md).

### Task 2: Design your header and create your data packet

**Description:** The sender micro:bit needs to add a header to each
message before sending. The message header will include:

- sender address

- receiver address

Your final data packet will have the following information:

- header
- your message

**Instruction:** First construct the sender and receiver addresses. With your teammate, pick two-letter strings as micro:bit addresses. You need one address for your micro:bit, and one address for your teammate’s micro:bit. For example, you can use your initials: These are “CS” and “AK” for the authors of this book. **Important! Your addresses should be unique across all the addresses of micro:bits that are in the same room
with you.**

Next, join the strings for sender and receiver addresses to create the message
header.

Pick a string as your message. For example: “Hello”. Join your message string with your header.

Now, your sender micro:bit is ready to send unicast packets.

### Task 3: Receive a packet

**Description:** When the receiver micro:bit receives a packet, it
decides whether to receive or ignore the packet. Notice that the
receiver micro:bit receives a single string, but it knows that this
string is made up of:

- Sender address: first 2 letters

- Receiver address: next 2 letters

- Sender’s message: the rest of the string

The receiver needs to use this information to decide which packets are for itself.

**Instruction:** Divide the received string into the *sender address*, *receiver address*, and *sender’s message* variables.

Check if the *receiver address* is equal to your micro:bit’s address. If it is, then your micro:bit is the rightful receiver. Display the sender address and the message on your display. If your micro:bit is not the receiver, be a good citizen, and ignore the message.

### Task 4: Filter senders

**Description:** Sometimes, you may not want to receive messages just from anybody. For this, you will write a program so that you only receive messages from two people you know. We will call this your *allow-list* (often referred to as a *whitelist*).

**Instruction:** Extend the receiver program to also check the *sender address* field in the header. Check whether this address is in your allow-list. If yes, display the sender address and the message. If not, ignore the message. Test your program with addresses in and out of your whitelist.

Extended activity
-----------------

!!! attention "Exercise 1"
	You may have written two separate programs: one for the receiver and one for the sender. Change your program so that both micro:bits can send and receive.

!!! attention "Exercise 2"
	Did you try listening out for messages sent from other micro:bits in your class? How could your program achieve this? Is this the right thing to do? How might you protect your messages from others snooping?

!!! attention "Exercise 3"
	In this chapter, we have covered one way to do a unicast: Putting sender and receiver addresses in a data packet header. But there is another way. Remember [Group communication: one to many](../groupcommunication/groupcommunication.md). If you set your group to be only for your pair of micro:bits, then this is like you are unicasting. What are the limitations of doing unicast like this? **Hint: Think about how many possible group IDs there are. Would this be enough for everyone in the world who has a micro:bit?**

Problems
--------

1. In what ways is unicast like broadcast and group communication? In what ways is it different?

2. Which ones are not IP addresses?

    1. -1.0.0.1

    2. 278.0.10.0

    3. 104.20.14.61

    4. 127.0.0.1

    5. 161.23.84;18

    6. 161.73.246.13

    7. 104.20.14.61.15

3. In this chapter, you used two-letter strings for your addresses. How many different people can you unicast using this address size?

4. When selecting an address size for your message header, can you pick any size you like? In your program, what happens if you increase your address size to 10 letters? Do you see any benefits? Or are there any limitations?

5. How does the size of a data packet header affect the actual packet size? If your data packet size were 100 Bytes, and your header size were 10 Bytes, how big could your messages be? What happens if the header size increases to 50 Bytes?

Solutions
---------

Solutions for this chapter can be found in the [Github directory](/code)

Resources
---------

- Video: IP addresses and DNS (code.org) -
    <https://youtu.be/5o8CwafCxnU>

- Video: IP addresses (CommonCraft) -
    <https://www.commoncraft.com/video/ip-addresses>

- BBC bitesize networks -
    <http://www.bbc.co.uk/education/topics/zjxtyrd>
