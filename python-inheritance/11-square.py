#!/usr/bin/python3
"""
11. Square #2
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Representation """
    def __init__(self, size):
        """ Cosntructor """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
