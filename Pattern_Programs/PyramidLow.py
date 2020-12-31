number = int(input("Enter the number of lines:"))
x =0
for i in range(number,0,-1):
    for j in range(x):
        print(" ",end = " ")
    x+=1
    for j in range(i):
        print("*  ",end=" ")
    print()
