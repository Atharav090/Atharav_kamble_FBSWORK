# Write a program find reverse of a number
def reverse_number(num):
    rev = 0
    while num > 0:
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    return rev
number = int(input("Enter a number: "))
result = reverse_number(number)
print(f"The reverse of {number} is {result}")