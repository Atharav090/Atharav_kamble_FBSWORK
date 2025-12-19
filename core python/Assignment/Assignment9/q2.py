# Write a program to check if given number is Armstrong or not using recursive function.
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
def is_armstrong(n, num_digits, original_n):
    if n == 0:
        return 0
    digit = n % 10
    return (digit ** num_digits) + is_armstrong(n // 10, num_digits, original_n)
number = int(input("Enter a positive integer: "))
num_digits = count_digits(number)
armstrong_sum = is_armstrong(number, num_digits, number)
if armstrong_sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")