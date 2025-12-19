# Write a program to print Fibonacci series using recursion. without list
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
number = int(input("Enter the number of terms in Fibonacci series: "))
print("Fibonacci series:")
for i in range(number):
    print(fibonacci(i), end=' ')
    
