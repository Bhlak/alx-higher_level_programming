#!/usr/bin/python3
"""Defines a class Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle with a
           width and a height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Prints area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Print() and str() format representation"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
