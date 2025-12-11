# WAP to print armstrong numbers between given range (if a number is equal to the sum of its own digits, each raised to power of the total number of digits, then it is an armstrong number)
# take input
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))
# loop through range
for num in range(start, end + 1):
    # number of digits
    order = len(str(num)) #to find number of digit and power to which each digit is to be raised 
    sum = 0
    temp = num
    # extract digits and calculate sum of powers
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    # check if armstrong
    if num == sum:
        print(num)