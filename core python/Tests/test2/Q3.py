# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times. circular sectin has redius 20m and rectangle length is 50m and breadth is 40m. if a cost of barbed wire is 35Rs./m then calculate the total cost of fencing the field.

# given data
radius = 20
length = 50
breadth = 40
pi = 3.14
cost_per_meter = 35

# calculations
circumference_semicircle = (2 * pi * radius) / 2
rectangle_perimeter = (2 * length) + breadth

# cost of fencing
total_fencing_length = (circumference_semicircle + rectangle_perimeter) * 5
total_cost = total_fencing_length * cost_per_meter
print(f'The total cost of fencing the field is Rs. {total_cost}')
