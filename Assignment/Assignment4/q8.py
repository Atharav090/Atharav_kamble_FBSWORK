# WAP to find which number are divisible by 7 and multiple of 5 in given range
# take input
r = int(input("Enter a number to set range from 1: "))
# loop
for i in range(1, r+1):
    # condition
    if(i % 7 == 0 and i % 5 == 0):
        print(i)