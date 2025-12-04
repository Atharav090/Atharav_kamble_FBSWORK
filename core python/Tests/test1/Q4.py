# calculate the cost of painting the following building's wall (both interior or exterior). accept area (one wall) and cost of both interior and exterior wall

# take inputs
area_one_wall = float(input("Enter the area of one wall in square meters: "))
cost_interior_per_sqm = float(input("Enter the cost of painting interior wall per square meter: "))
cost_exterior_per_sqm = float(input("Enter the cost of painting exterior wall per square meter: "))

# calculate total area for 4 walls
total_area_interior = area_one_wall * 8
total_area_exterior = area_one_wall * 7

# calculate cost for interior and exterior painting
cost_interior = cost_interior_per_sqm * total_area_interior
cost_exterior = cost_exterior_per_sqm * total_area_exterior

# find total cost 
cost = (cost_interior + cost_exterior) * 2

#Display output

print(f'The cost for painting two buidings is {cost} Rs.')  
