#!/usr/bin/python3
"""
8. Rectangle
"""


class Rectangle(BaseGeometry):
    """ BaseGeometry Class """
    def __init__(self, width, height):
        """ Cosntruct """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
