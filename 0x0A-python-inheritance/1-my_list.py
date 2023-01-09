#!/usr/bin/python3
"""Defines a subclass to a Class list"""


class MyList(list):
    """Defines a class Mylist with a list superclass"""
    def __init__(self):
        """Initializes an object of MyList while initializing
           the superclass list.
        """
        super().__init__()

    def print_sorted(self):
        """Prints a list of the MyList object sorted
           in ascending order.
        """
        print(sorted(self))
