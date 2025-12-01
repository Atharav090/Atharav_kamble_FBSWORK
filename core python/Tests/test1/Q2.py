# WAP to calculate simple interest
# Take inputs
p = int(input("Enter the principal:"))
r = int(input("Enter the rate:"))
t = int(input("Enter the period of time in years:"))

# calculate the simple interest
si = (p * r * t)/100


# Display output
print(f'Simple interest on Principal: {p}, Rate: {r} and for {t} years of time period is {si}')


