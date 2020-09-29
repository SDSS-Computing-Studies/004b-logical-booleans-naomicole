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
a=int(a)

b=math.sqrt(a)
b=round(b,4)
b=int(b)
b1=b**2

c=a**(1/3)
c=round(c,4)
c=int(c)
c1=c**3

if b1 ==a and c1 ==a:
    print(a, end=" ")
    print("xx is both a perfect square and a perfect cube")

elif b1==a and c1!=a:
    print(a, end=" ")
    print("xx is only a perfect square")

elif b1!=a and c1==a:
    print(a, end=" ")
    print("xx is only a perfect cube")