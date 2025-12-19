# Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms

def fibonacci_series(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
fibonacci_series(n)