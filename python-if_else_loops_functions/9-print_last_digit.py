#!/usr/bin/python3
#9-print_last_digit.py

def print_last_digit(number):
    """
    Function that prints the last digit of a number.
    """
    lastnum = abs(number) % 10

    print(f"{lastnum}", end="")

    return (lastnum)
