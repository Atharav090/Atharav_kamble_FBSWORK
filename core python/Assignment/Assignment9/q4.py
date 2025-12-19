# Write a program to find sum of n numbers using recursion.
def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)
number = int(input("Enter a positive integer: "))
result = sum_of_numbers(number)
print(f"The sum of first {number} natural numbers is: {result}")