x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum_series = 0

for i in range(1, n + 1):
    term = (i * x) / (2*i - 1)

    if i % 2 == 0:   # even term → negative
        sum_series -= term
    else:            # odd term → positive
        sum_series += term

print("Sum of series =", sum_series)