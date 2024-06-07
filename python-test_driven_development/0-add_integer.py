#!/usr/bin/python3
# 0-add_integer.py
"""
Here is de excersice of add two integers
"""


def add_integer(a, b=98):
    """
    Function which return the value of add two integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
