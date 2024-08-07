#!/usr/bin/python3
"""
9. Student to JSON
"""


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Student Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves a dictionary representation of a Student instance """
        return self.__dict__
