# WAP to accept distance in KM and convert it into meters and centimeters
# take input
km = float(input("Enter distance in kilometers: "))

# convert km to m and cm
meters = km * 1000
centimeters = km * 100000

# Display output
print(f"Distance in meters: {meters} m")
print(f"Distance in centimeters: {centimeters} cm")