# Write a program to reverse a given number using recursive function.
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        rev = rev * 10 + n % 10
        return reverse_number(n // 10, rev)
number = int(input("Enter a positive integer: "))
reversed_num = reverse_number(number)
print(f"The reverse of {number} is: {reversed_num}")

