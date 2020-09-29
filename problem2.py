#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
x=input("Enter an integer: ")
x=float(x)

y=input("Enter an integer: ")
y=float(y)

if x>y:
    x1=x/y
    x2=int(x1)

    if (x1-x2)==0:
        print(y, end=" ")
        print("is a factor of",end=" ")
        print(x)

    else:
        print(y,end=" ")
        print("is not a factor of",end=" ")
        print(x)

elif y>x:
    y1=y/x
    y2=int(y1)

    if (y1-y2)==0:
        print(x,end=" ")
        print("is a factor of",end=" ")
        print(y)

    else:
        print(x,end=" ")
        print("is not a factor of",end=" ")
        print(y)