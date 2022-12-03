#!/usr/bin/python3
def remove_char_at(str, n):
    word = ""
    idx = 0
    for i in str:
        if idx == n:
            continue
        word += i
        idx += 1
    return word
