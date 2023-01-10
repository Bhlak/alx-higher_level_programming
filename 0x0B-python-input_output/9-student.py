#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes an instance of the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of the
        current instance
        """
        return self.__dict__
