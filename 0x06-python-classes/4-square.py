#!/usr/bin/python3

"""Defines a class 'Square'"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """

        Initializes a new square with a private size.

        Args:

            size (int): The size of the new square.

        """
        self.size = size

    @property
    def size(self):
        """Get size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__size ** 2)
