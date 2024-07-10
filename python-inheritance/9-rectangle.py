#!/usr/bin/python3
"""
9. Full rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ BaseGeometry Class """
    def __init__(self, width, height):
        """ Cosntruct """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Rectangle description """
        return f"[Rectangle] {self.__width}/{self.__height}"
