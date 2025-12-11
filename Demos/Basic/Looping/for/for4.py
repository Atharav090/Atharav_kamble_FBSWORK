# WAP alternate numbers sum
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1, 2):
    print(f'{sum} + {i} =', end = ' ')
    sum = sum + i
    print(sum)
print(f'final sum of the number is: {sum}')