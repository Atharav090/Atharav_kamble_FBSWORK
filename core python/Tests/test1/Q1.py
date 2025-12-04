# WAP to find area and perimeter of following figure. (rectangle joined with semi circle on the right)
# take inputs
l = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
r = int(input("Enter the radius:"))

# calculate area and perimeter
area_rectangle = l * b
area_semi_circle = (3.14 * r * r) / 2

perimeter_rect = 2*l + b
perimeter_semi_circle = 3.14 * r 

# total area and perimeter
area = area_rectangle + area_semi_circle
perimeter = perimeter_rect + perimeter_semi_circle

# printing output
print(f'Area of the figure is {area}')
print(f'Perimeter of the figure is {perimeter}')
