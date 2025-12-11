# WAP to check whether triangle is equilateral, isoceles, or scalene.
# take inputs
s1 = int(input("Enter the first side of triangle: "))
s2 = int(input("Enter the second side of triangle: "))
s3 = int(input("Enter the third side of triangle: "))

# conditions
# Equilateral - All three sides are equal.
# Isoceles - Two sides are equal.
# Scalene - all three sides are different.

if(s1 == s2 == s3):
    print(f'Triangle is equilateral triangle.') 
elif(s1 == s2 or s2 == s3 or s1 == s3):
        print(f'Triangle is isoceles triangle.')
else:
    print(f'Triangle is scalene triangle')