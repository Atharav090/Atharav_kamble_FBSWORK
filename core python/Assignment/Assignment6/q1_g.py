k =65
for i in range(1,6):
    for j in range(1, 7-i):
        print(" ", end=" ")
    for j in range(1, i+1):
        print(chr(k), end=" ")
        k += 1
    for j in range(1, i):
        print(chr(k), end=" ")
        k += 1
    k =65
    print()