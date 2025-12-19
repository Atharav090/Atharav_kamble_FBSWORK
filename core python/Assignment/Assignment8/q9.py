# Write a program to check if entered number is a palindrome or not.
def is_palindrome(num):
    original_num = num
    rev = 0
    while num > 0:
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    return rev == original_num
number = int(input("Enter a number: "))
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")