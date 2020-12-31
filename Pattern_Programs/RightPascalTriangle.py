number = int(input("Enter the number:"))
x = 0;
for i in range(number*2-1):
    j = 0
    if i >= number:
        x = x-1
    else :
        x = x+1
    for j in range(x):
        print("# ", end=" ")
        j += 1
    i += 1

    print()
