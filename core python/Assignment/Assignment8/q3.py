# Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

def addition_n(n):
    add = 0
    for i in range(1, n+1):
        add += i
    return add

def add_fact_n(n):
    sum_fact = 0
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i       
    sum_fact += fact
    return sum_fact

def add_exp_n(n):
    sum = 0
    exp = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
           exp = i ** j
    sum += exp
    return sum


print(addition_n(10))
print(add_fact_n(10))
print(add_exp_n(10))