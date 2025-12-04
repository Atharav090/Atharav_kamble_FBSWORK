# WAP t print sum of the series upto n
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(f"sum of the numbers till {n} is {sum}")