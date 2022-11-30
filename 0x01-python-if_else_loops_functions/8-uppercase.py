#!/usr/bin/python3
def uppercase(str):
    new = ""
    for i in str:
        temp = ord(i)
        if ord(i) >= 97 and ord(i) <= 123:
            temp -= 32
        new += chr(temp)
    print("{:s}".format(new))
