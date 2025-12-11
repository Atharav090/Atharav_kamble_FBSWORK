# WAP to check if given number is strog number (if number is equals to sum of factorial of it's all digits then it is a perfect number)
# take inputs
num = int(input("Enter a number:")) #145
temp = num #145
sum = 0
# take digits out
while temp > 0:
    d = temp % 10
    temp //= 10
    fact = 1
    # factorial
    for i in range(d, 0, -1):
        fact = fact * i
    sum = sum + fact

if(num == sum):
    print(f"{num} is a strong number")
else: 
    print(f"{num} is not a strong number")


