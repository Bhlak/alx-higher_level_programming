#!/usr/bin/python3

"""Defines a class 'Rectangle'"""


class Rectangle:
    """
    Defines a Rectangle

    Attributes:
        number_of_instances(int): Tracks number of class objects
        print_symbol(any): Symbol used to represent strings
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle

        Args:
            width(int): Width of the rectangle instance
            height(int): height of the rectangle instance
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            arr.append(str(self.print_symbol)*self.width)
            if temp != 1:
                arr.append('\n')
            temp -= 1
        return ("".join(arr))

    def __repr__(self):
        fin = "Rectangle(" + str(self.width)
        fin += ", " + str(self.height) + ")"
        return fin

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
