from microbit import *
import radio
import random

radio.on()

master_name = "JG"
other_masters = ["CS", "AK"]

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
    available = False
    for i in range(checks):
        radio.send(master_name + "?")
        for j in range(wait): # How long to wait to see if taken
            message = radio.receive()
            if message is not None:
                if message == master_name: # Once master is found, stop searching
                    available = True
                    return available
            sleep(1)
    return available

group = findAvailableGroup(3, 250)
display.show(str(group))
