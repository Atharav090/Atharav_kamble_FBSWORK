

for i in range(1,5):
    # Print leading spaces
    for j in range(4-i):
        print(" ", end="")
    
    # Initialize first value in a row
    val = 1
    for k in range(1, i+1):
        print(val, end=" ")
        val = val * (i - k) // k  # Calculate next value in the row
    
    print()  