#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """
    Function that prints a string in uppercase followed by a new line.
    """
    aux_str = ""

    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        aux_str += i

    print("{}".format(aux_str))
