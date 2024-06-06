#!/usr/bin/python3
# 0-add_integer.py
# """ Here comes a little description """

def add_integer(a, b=98):
    if not(isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not(isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))