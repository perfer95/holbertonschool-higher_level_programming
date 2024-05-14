#!/usr/bin/python3
#3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """
    function that prints all integers of a list, in reverse order.
    """
    len_list = len(my_list)

    for i in range(-1, -len_list - 1, -1):
        print("{:d}".format(my_list[i]))
