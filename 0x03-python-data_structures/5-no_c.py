#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    new_str = [i for i in my_string if i != 'c' or i != 'C']
    return ''.join(new_str)
