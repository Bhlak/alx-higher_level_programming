#!/usr/bin/python3
def print_reverssed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[i]))
