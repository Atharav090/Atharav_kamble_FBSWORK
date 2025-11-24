# Write a program to swap two numbers without using third variable.
# Taking input from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
# Swapping the values
# a = a + b
# b = a - b
# a = a - b

# Other technique (It is not widely used)
a , b = b , a

# Displaying the swapped values
print(f'After swapping, first number (a) is: {a}')
print(f'After swapping, second number (b) is: {b}')