# WAP to print sum of digit number
num = int(input("Enter a number:"))
sum = 0
while(num > 0):
    rem = num % 10
    sum = sum + rem
    num //= 10

print(f'addition of digits of given number is {sum}')
