# Sum of all prime numbers between 1 to n
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter n: "))
prime_sum = 0

for i in range(2, n + 1):
    if is_prime(i):
        prime_sum += i

print("Sum of all prime numbers between 1 and", n, "is:", prime_sum)
