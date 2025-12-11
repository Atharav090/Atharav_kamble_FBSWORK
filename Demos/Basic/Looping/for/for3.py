# WAP to calculate sum of series / sum of first n numbers.
n = int(input("Take the value of n: "))
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(f'sum of the number till n = {n} is {sum}')