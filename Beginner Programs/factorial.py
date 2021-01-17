"""
    Factorial both iterative and recursive
"""

def factrecursive(value):
    if (value == 0 or value == 1) :
        return 1
    return value * factrecursive(value - 1)

def factiterative(value) :
    if (value == 0 or value == 1):
        return 1
    c = 1
    for i in range(1,value+1):
        c = c * i
    return c

number = int(input("Enter the number to find the factorial:"))
print(f'Iterative function : \n Factorial of {number} is {factiterative(number)}')
print(f'Recursive function : \n Factorial of {number} is {factrecursive(number)}')
