#!/usr/bin/python3

"""Defines a class 'Square'"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """

        Initializes a new square with a private size and position.

        Args:

            size (int): The size of the new square.
            position (tuple): The coordinates of the square.

        """
        self.position = position
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not all(isinstance(num, int) for num in value) or
                len(value) != 2 or
                not all(i >= 0 for i in value)):
            raise TypeError("position must br a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        length = self.size
        if length == 0:
            print()
            return
        j = length
        pos = self.position
        temp = pos[1]
        while temp > 0:
            print("")
            temp -= 1
        while length > 0:
            print(" "*pos[0], end="")
            print("#"*j)
            length -= 1
