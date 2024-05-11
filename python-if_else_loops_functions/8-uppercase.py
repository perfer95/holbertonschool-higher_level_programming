#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """
    Function that prints a string in uppercase followed by a new line.
    """
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            print("{}".format(chr(ord(i) - 32)), end="")
    print("")
