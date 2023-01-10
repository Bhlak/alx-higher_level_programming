#!/usr/bin/python3
"""Inserts line of text into file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after every instance of a string
       to the original file.
    """
    text = ""
    with open(filename, 'r') as f:
        for line in f:
            text += line
            if line == search_string:
                text += new_string
    with open(filename, 'w') as f:
        f.write(text)
