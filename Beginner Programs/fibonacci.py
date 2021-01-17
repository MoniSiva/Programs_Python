"""
    Fibonacci Series
"""

def fib(index):
    a = 0
    b = 1
    if index < 1:
        return
    elif index == 1:
        print(a)
        return
    else :
        print(a," ",b,end =" ")
    for i in range(index-2):
        c = a + b
        print(" ",c,end = " ")
        a = b
        b = c

n =(int(input("Enter the number of series to print :")))
print(f'Fibonacci series for {n} numbers ::')
fib(n)