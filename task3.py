#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
a=input("Enter a number of any type: ")
a=float(a)

if a>0:
    print(a, end=" ")
    print("is a positive integer.")

elif a<0:
    print(a, end=" ")
    print("is not a positive integer.")