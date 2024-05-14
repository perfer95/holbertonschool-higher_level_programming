#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """
    Function that prints all integers of a list.
    """
    for i in range(0, len(my_list) + 1):
        print("{:d}".format(my_list[i]))
