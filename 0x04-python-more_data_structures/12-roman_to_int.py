#!/usr/bin/python3
from functools import reduce 
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    for i in range(len(roman_string)-1, -1, -1):
        num = numerals[roman_string[i]]
        if 3*num < total:
            total -= num
        else:
            total += num
    return total
