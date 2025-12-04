# WAP to calculate the total cost of painting the interior of the building with four equal sized wall

# take input for area
areaOfWall = int(input("Enter the size of one wall: "))
cost_interior_per_sqm = float(input("Enter the cost of painting interior wall per square meter: "))

areaOfBuilding = areaOfWall * 4

cost_interior = cost_interior_per_sqm * areaOfBuilding
print(f'To paint the building with {areaOfWall} size of one wall, it will cost {cost_interior}Rs.')