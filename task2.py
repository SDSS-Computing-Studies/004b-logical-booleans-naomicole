#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""

import math

a=input("Enter a number: ")
a=float(a)

b=math.sqrt(a)
c=a**(1/3)

if b!=float(b) and c!=float(c):
    print("xx is both a perfect square and a perfect cube")

elif b!=float(b) and c!=float(c):
    print("xx is only a perfect square")

elif b!=float(b) and c==float(c):
    print("xx is only a perfect cube")