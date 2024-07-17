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
        print(f"Name: {self.name}\nAge: {self.age}\n"
                f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

    @classmethod
    def deserialize(cls, filename):
        """ Deserialize file"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            return None
