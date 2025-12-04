# WAP to check if given number is perfect number. (if a number is equal to sum of it's proper divisior then it is a perfect number)
# take input
num = int(input("Enter a number to check if it is perfect number or not: "))
sum = 0

for i in range(1, num):
    if(num % i == 0):
        print(i)
        sum = sum + i
if(sum == num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

