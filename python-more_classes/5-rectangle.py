#!/usr/bin/python3
"""
5. Detect instance deletion
"""


class Rectangle:
    """
    Class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangugle attributes """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Calculate area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculate perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Rectangle informal representation """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []

        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """ Rectangle formal representation """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Message delete """
        print("Bye rectangle...")
