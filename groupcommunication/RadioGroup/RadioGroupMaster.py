from microbit import *
import radio
import random

radio.on()

master_name = "JG"
other_master_queries = ["CS?", "AK?"]

# Finds and configures the radio to an available group
def findAvailableGroup(checks, max_wait):
    # Raises error if parameters aren't positive integers greater than zero
    if isinstance(checks, int) == False or isinstance(max_wait, int) == False:
        raise ValueError("Parameters must be positive integers greater than zero")
    elif checks <= 0 or max_wait <= 0:
        raise ValueError("Parameters must be positive integers greater than zero")

    available = False
    while available == False:
        try_group = random.randint(1, 255) # Chooses random group to test, lower upper bound when testing
        radio.config(group = try_group) # Reconfigures the radio to that group
        wait = random.randint(0, max_wait) # Random amount of time to check for a response
        available = checkGroup(checks, wait) # Checks if group is in use

    return try_group # Returns the ID of the available group currently configured to

# Checks to see if group currently on is available up to 'checks' times
# User should not call this function
def checkGroup(checks, wait):
    available = True
    for i in range(checks):
        radio.send("TAKEN?")
        for j in range(wait): # How long to wait to see if taken
            message = radio.receive()
            if message is not None:
                # If group is taken, try a different group
                if message == "TAKEN?" or message in other_master_queries or message == "GROUP TAKEN": # Other messages are ignored
                    available = False
                    return available
            sleep(1)
    return available

group = findAvailableGroup(3, 250)
while True:
    message = radio.receive()
    if message is not None:
        if message == (master_name + "?"):
            radio.send(master_name) # Notifies slave microbits it is the correct group
        else:
            radio.send("GROUP TAKEN") # Other microbits told group is full
    display.show(str(group))
