# Write a program to find factorial using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a positive integer: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")