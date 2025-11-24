# Write a program to reverse three-digit number.
# Taking input from the user
num = int(input("Enter a three-digit number: "))
# Extracting digits
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
# Reversing the number
reversed_num = (units * 100) + (tens * 10) + hundreds
# Displaying the reversed number
print(f'The reversed number is: {reversed_num}')