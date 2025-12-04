# WAP to reverse a three digit number

num = int(input("Enter a number"))
rev = 0
while(num < 0):
    d = num % 10
    d = str(d)
    rev = rev + d
    no //= 10
print(rev)
