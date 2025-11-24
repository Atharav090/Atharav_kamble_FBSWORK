# WAP to calculate area of triangle and rectangle
# take inputs
l = int(input("Enter the length of rectangle: "))
b = int(input("Enter the breadth of rectangle: "))
base = int(input("Enter the base of triangle: "))
height = int(input("Enter the height of triangle: "))

# calculate area of rectangle
area_rectangle = l * b
# calculate area of triangle
area_triangle = 1/2 * base * height
# display results
print(f'Area of the rectangle is {area_rectangle}')
print(f'Area of the triangle is {area_triangle}')
