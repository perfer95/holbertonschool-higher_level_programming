#/usr/bin/python3
"""
1. Shapes, Interfaces, and Duck Typing
"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ Shape Class """
    @abstractmethod
    def area(self):
        """ Calculate Area """
        pass

    @abstractmethod
    def perimeter(self):
        """ Calculate Perimeter"""
        pass

class Circle(Shape):
    """ Circle Class"""
    def __init__(self, radius):
        """ Contructor """
        self.radius = radius

    def area(self):
        """ Calculate Area """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """ Calculate Perimeter"""
        if self.radius < 0:
            return -(pi * (abs(self.radius) * 2))
        return pi * (self.radius * 2)

class Rectangle(Shape):
    """ Rectangle Class"""
    def __init__(self, width, height):
        """ Constructor """
        self.width = width
        self.height = height

    def area(self):
        """ Calculate Area """
        return self.width * self. height

    def perimeter(self):
        """ Calculate Perimeter"""
        return (self.width * 2) + ( self. height * 2)


def shape_info(obj):
    """ Printer data"""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
