#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """
    function that removes all characters c and C from a string.
    """
    new_list = []

    for i in range(0, len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            new_list += my_string[i]
    return new_list
