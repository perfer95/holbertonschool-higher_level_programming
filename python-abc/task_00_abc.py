#/usr/bin/python3
"""
0. Abstract Animal Class and its Subclasses
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Abstrac Class """
    @abstractmethod
    def sound(self):
        """ Sound Abstrac Method"""
        pass

class Dog(Animal):
    """ Dog class """
    def sound(self):
        return "Bark"

class Cat(Animal):
    """ Cat class """
    def sound(self):
        return "Meow"
