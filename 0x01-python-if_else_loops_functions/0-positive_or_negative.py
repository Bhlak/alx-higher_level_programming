#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    text = "is positive"
elif number == 0:
    text = "is zero"
else:
    text = "is negative"

print(f"{number} {text}")
