#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    """
    Function that returns a new dictionary with all values multiplied by 2
    """
    new_dictionary = {key: value * 2 for (key, value) in a_dictionary.items()}

    return new_dictionary
