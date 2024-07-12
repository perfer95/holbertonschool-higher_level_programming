#!/usr/bin/oython3
"""
5. The Mystical Dragon - Mastering Mixins
"""


class SwimMixin:
    """ SwimMixin Class """
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """ FlyMixin Class """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """ Dragon Class """
    def roar(self):
        print("The dragon roars!")
