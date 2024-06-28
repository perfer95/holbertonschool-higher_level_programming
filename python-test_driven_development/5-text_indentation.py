#!/usr/bin/python3
"""
5-text_indentation.py
"""


def text_indentation(text):
    """
    def text_indentation(text): ".", "?" and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    end = 0

    for i in text:
        if i in ".?:" or ((end + 1) == len(text)):
            end += 1
            if not (text[start] == " " and text[end - 1] == " "):
                print(text[start:end], end="")
            start = end
            if i in ".?:":
                print("\n")
        elif text[start] == " ":
            start += 1
            end += 1
        else:
            end += 1
