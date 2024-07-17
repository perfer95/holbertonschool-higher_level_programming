#!/usr/bin/python3
"""
1. Pickling Custom Classes
"""
import pickle


class CustomObject:
    """ CustomObject Class """
    def __init__(self, name, age, is_student):
        """ CustomObject Contruct """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """ Print attributes """
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """ Serialize """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        """ Deserialize file"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except:
            return None
