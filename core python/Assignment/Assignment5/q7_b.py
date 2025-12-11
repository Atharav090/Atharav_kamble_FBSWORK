# Write a program to solve the following series :
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
N = int(input("Enter N: "))
total = 0
power = 1

for i in range(1, N + 1):
    power *= N       # multiply by N each time → N^i
    total += power

print("Sum =", total)
