# WAP to input angles of triangle and check whether triangle is valid or not
# Take inputs
a1 = int(input("Enter the first angle of the triangle:"))
a2 = int(input("Enter the second angle of the triangle:"))
a3 = int(input("Enter the third angle of the triangle:"))

# addition of triangle should be 180 degrees
sum_of_angles = a1 + a2 + a3

# conditions
if(sum_of_angles == 180):
    print("Triangle is valid.")
else: 
    print("Triangle is not valid")
