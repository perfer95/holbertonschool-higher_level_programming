#!/usr/bin/python3
# 7-islower.py

def islower(c):
    """
    Function that verify if a char variable(alpha) is lower
    Return True if c is lowercase
    Return False if c is not lowercase
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else
        return False
