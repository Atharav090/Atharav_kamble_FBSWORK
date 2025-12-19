# WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def is_armstrong_number(num):
    order = len(str(num))
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    return total == num
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")