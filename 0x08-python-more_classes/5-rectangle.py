#!/usr/bin/python3

"""Defines a class 'Rectangle'"""


class Rectangle:
    """Defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle

        Args:
            width(int): Width of the rectangle instance
            height(int): height of the rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        arr = []
        temp = self.height
        while temp > 0:
            arr.append("#"*self.width)
            if temp != 1:
                arr.append('\n')
            temp -= 1
        return ("".join(arr))

    def __repr__(self):
        fin = "Rectangle(" + str(self.width)
        fin += ", " + str(self.height) + ")"
        return fin

    def __del__(self):
        print("Bye rectangle...")
