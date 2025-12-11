# WAP to print all numbers in range divisible by given number
# take inputs
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
num = int(input("Enter a divisor number: "))

for i in range( start, end+1):
    if(i % num == 0):
        print(i)
