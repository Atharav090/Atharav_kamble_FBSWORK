# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.
# take input
basic = int(input("Enter the basic salary of the employee: "))
# Add DA to basic
DA = 0.10 * basic
# Add TA to basic
TA = 0.12 * basic
# Add HRA to basic
HRA = 0.15 * basic
# calculate total salary
total_salary = basic + DA + TA + HRA
# display result
print(f'The total salary of the employee is {total_salary}')