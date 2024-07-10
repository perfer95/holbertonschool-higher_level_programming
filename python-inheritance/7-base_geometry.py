#!/usr/bin/python3
"""
7. Integer validator
"""


class BaseGeometry():
    """ BaseGeometry Class """
    def area(self):
        """ Method to calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value if is a integer """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))