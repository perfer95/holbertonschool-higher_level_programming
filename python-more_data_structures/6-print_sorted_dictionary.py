#!/usr/bin/python3
# 6-print_sorted_dictionary.py

def print_sorted_dictionary(a_dictionary):
    """
    Function that prints a dictionary by ordered keys.
    """
    tupla_sort = sorted(a_dictionary.keys())

    for i in tupla_sort:
        print("{}: {}".format(i, a_dictionary[i]))
