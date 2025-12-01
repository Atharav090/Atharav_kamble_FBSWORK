# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3 digit number to check if it is palindrome or not: "))

# storing a number in temporary variable
temp = num

# entracting digits (d1 will be last digit from number for eg. 123, 3 will be d1)
d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

# converting the number to string to concanate
d1 = str(d1)
d2 = str(d2)
d3 = str(d3)

reversed_number = d1+d2+d3
print(reversed_number)
# convert string to int again to compare. 
reversed_number = int(reversed_number)

if(temp == reversed_number):
    print(f'{temp} is a palindrome number.')
else :
    print(f'{temp} is not a palindrome number.')