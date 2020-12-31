number = int(input("Enter the number of lines:"))
x =1;
y = number-1
for i in range(number):
    for j in range(y):
        print(" ",end = " ")
    y -= 1
    for j in range(i+1):
        print("*  ",end = " ")

    print()
