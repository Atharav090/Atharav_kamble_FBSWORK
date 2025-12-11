# WAP to check whether triangle is valid or not
# take inputs
s1 = int(input("Enter the first side of triangle: "))
s2 = int(input("Enter the second side of triangle: "))
s3 = int(input("Enter the third side of triangle: "))

# conditions (addition of two sides of triangle is greated than third side then triangle is valid.)
if(s1 + s2 > s3):
    if(s1 + s3 > s2):
        if(s2 + s3 > s1):
            print(f'Triangle is valid.')
else: 
    print(f'Triangle is not valid')

