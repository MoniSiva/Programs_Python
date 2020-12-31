number = int(input("Enter the number : "))
for i in range(number):
    for j in range(number-i+1):
        print(" ",end = " ")
    for j in range(i+1):
        print("#",end = " ")
    print()
