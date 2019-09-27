Group communication: One to Many
================================

![Chapter 3 image](chapter3.png)

Introduction
------------

In the previous chapter, you experimented with broadcast: sending messages to everybody. In this chapter, you will learn about sending a
message so that it goes to a smaller group of people. This is an activity that is best carried out with a large group of friends or classmates so that you can experiment with different groups and group sizes.

Group communication (also known as multicast) is an interesting concept
and enables several of today’s Internet technologies. For
example, using this technology,  videos can be sent faster over the
Internet.

In this chapter, you will learn:

- The concept of *group communication* and *group* or *multicast
    address*
- When group communication is useful and when it isn’t

### What you’ll need

    2 micro:bits
    1 whiteboard/board
    Boardmarkers/post-it notes
    1 teammate

Background
----------

In the previous chapter, all micro:bits could receive messages from all the
other micro:bits in their vicinity. This might have got confusing (or amusing). Now,
let’s try limiting who you can send messages to and receive messages
from. This is called group communication. Group communication is used on
the internet to send to many people at the same time. For example,
Internet television and videoconferencing use group communication.

!!! hint "Definition 1: _Communications medium_"
	In group communication or multicast, a message
	is sent only to the computers in the group.

For this, the messages need to be labelled with a *group* or *multicast
address*.

!!! hint "Definition 2: _Group address_"
	A group or multicast address is a special address
	which says all devices in the group should receive this message.

To set a group address (or group ID), you will use
the *group* parameter that can be set  in the `radio.config()`
function.

The main challenge of this chapter is creating the actual groups for communication. Think about how computers learn about and join these groups.
What happens when a computer leaves a group? In this chapter, you will have a chance to think about these questions when you experiment with creating groups.

### **Further reading**

When configuring group IDs for micro:bits, you will notice that the group IDs range from 0 to 255. This is the decimal (base 10) representation of group IDs. But we can also write these group IDs in binary (base 2). For the binary case, we will need 8 bits to get to a maximum group ID of 255.

Let’s think about the binary representation of group IDs.
The figure below shows an example for the group ID 172 in 8 bits: 10101100. Notice that, we start reading bits from right to left. Each bit is numbered 1 to 8, corresponding to a power of two. The
rightmost bit, bit 1, means $2^0 = 1$.
Bit 2 means $2^1 = 2$ and we
continue like this until we reach bit 8, which means $2^7 = 128$. Each
bit location may contain either 0 or 1. To find the decimal value of
10101100, we need to do some maths.
For a bit location $x$, we multiply its
bit value with $2^{x-1}$. For bit
location 8, the bit value is 1, and we need to multiply $2^(8-1) =2^7=128$ with 1.
After doing this for all the bit locations, we add all the values we found.
The result of this addition is 172.

Now, check for the case 11111111. Is
it really equal to 255? For further reading, see the BBC Bitesize,
Binary revision page in the Resources section.

![Binary representation of group IDs.](BinaryAddress.png)

!!! note ""
	**Figure 1:** Binary representation of group IDs

Programming: Creating groups and messaging within groups
--------------------------------------------------------

In this chapter, you need to work together in pairs or small groups with at least two micro:bits in each group. You will complete two tasks to
program your micro:bits to send and receive messages within your group.

### Task 1: Create groups

**Description:** In this task, you will choose a unique group ID for
your group and configure your radios with this group ID. When
selecting the group IDs, you have to think about the best way to select
this number. **Hint: What would happen if two groups use the same
number, and how would you make sure that doesn’t happen?**

**Instruction:** Use the board and post-it notes to choose a group
ID. Make sure your group ID is not the same as any other group ID

### Task 2: Send and receive messages

**Description:** You will use the programs from the previous chapter [Broadcast communication:One to all](../broadcast/broadcast.md) to
send and receive messages in your group. You will change these programs
to count the number of messages you receive. This way, you will test
whether you receive messages only from your group.

**Instruction:** Use the Broadcast_Communications_sender.hex or your own code from the previous chapter [Broadcast communication:One to all](../broadcast/broadcast.md) to send numbers or strings. Write a receiver program
that increments a variable named `counter_number` each time it receives a number between 0-9 and increments a `counter_other` when it receives something else. When you press button A at the receiver, it displays the value of both counters. With
your group, test that you are receiving the correct number of messages.
Test together with other groups that when they are sending string messages, you are not receiving them.
(Note: If multiple groups were sending numbers, and their group numbers were the same, you may not be able to verify if and when you receive from a micro:bit outside your group.)

Extended activity
-----------------

!!! attention "Exercise 1"
	How easy or difficult would it be if micro:bits could create groups automatically themselves? How would they pick a group ID? How would they make sure nobody else had that number? Would broadcast be useful? Discuss with your teammates.

!!! attention "Exercise 2"
	Can a micro:bit be part of two groups or more? How would you program your micro:bit to do that?

Problems
--------

1. Fill in the blank in this sentence: “A one-to-many communication between one sender and a group of receivers is *---* communication.”

    1. unicast

    2. multicast

    3. broadcast

    4. none of the above

2. Let’s assume the group ID is 3 bits. For example, 010 is a group ID. What is the maximum number of groups can you have in a network?

3. If the group ID were 6 bits,  what is the largest group ID you could choose for your micro:bit?

4. “Compared to broadcast, the receivers in group communication receive more messages.” True or False?

Solutions
---------

Solutions for this chapter can be found in [the Github folder](/code)

Resources
---------

BBC Bitesize, Binary revision -
<http://www.bbc.co.uk/education/guides/z26rcdm/revision>
