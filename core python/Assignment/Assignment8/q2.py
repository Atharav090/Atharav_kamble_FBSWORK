# Write a program to calculate area of circle
def calculate_area_circle(r):
    pie = 3.14
    area = (2 * pie * (r * r))
    return area

r = int(input("Enter the radius: "))
print(f"Area of circle: {calculate_area_circle(r)}")