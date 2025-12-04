# WAP to accept year from user and check if  it is a leap year or not.

# Take user inputs
year = int(input("Enter a year: "))

# conditions for leap year
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(f'Year {year} is a Leap year')
        else:
            print(f'Year {year} is not a Leap year')
    else:
        print(f'Year {year} is a Leap year')
else: 
    print(f'Year {year} is not a Leap year')
     