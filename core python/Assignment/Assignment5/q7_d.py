# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = int(input("Enter value of a: "))
S = 0
power = 1

for i in range(1, 11):
    power *= a              # gives a^i
    S += power / i

print("Sum S =", S)
