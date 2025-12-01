# Check a number if it is neutral, positive, or negative 

num = int(input("Enter a number:"))

# conditions (elif ladder)
if(num == 0):
    print(f'{num} is a neutral number')
elif(num > 0):
    print(f'{num} is a positive number')
else:
    print(f'{num} is a negative number')