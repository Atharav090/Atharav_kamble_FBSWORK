# Write a program to print prime numbers between 1 to 100.
num = 1
while(num<=100):
    for i in range(2, num):
        if(num % i != 0):
            print(num)
        break
    num += 1