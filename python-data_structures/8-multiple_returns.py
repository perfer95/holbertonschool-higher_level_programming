#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """
    Function that returns a tuple with the length of a string
    and its first character.
    """
    length = (len(sentence), )
    f_char = ""

    if length[0] == 0:
        return 0, None
    else:
        f_char = sentence[0]
        return length[0], f_char
