# Write a program to find sum of digits of a number.

def sum_of_digit(num):
    total = 0
    while num > 0:
        d = num % 10
        total += d
        num = num // 10
    return total

number = int(input("Enter a number: "))
result = sum_of_digit(number)
print(f"The sum of digits of {number} is {result}")