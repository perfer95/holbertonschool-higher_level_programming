#!/usr/bin/python3
"""
10. Student to JSON with filter
"""


class Student:
    """ Student Class """
    def __init__(self, first_name, last_name, age):
        """ Student Constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if isinstance(attrs, list) and \
                all(isinstance(ele, str) for ele in attrs):
            """ dictionary comprehension """
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
