# Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def sum_of_factorials(n):
    if n == 1:
        return factorial(1)
    else:
        return factorial(n) + sum_of_factorials(n - 1)
n = int(input("Enter a positive integer: "))
result = sum_of_factorials(n)
print(f"The sum of the series 1! + 2! + ... + {n}! is: {result}")