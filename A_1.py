# Ask user for value for V AND R
v = float(input("Enter voltage:"))
r = float(input("Enter resistance:"))

# Check if resistance is acceptable
if r <= 0:
    print("Invalid resistance")
else:
    # Calculate current using formula
    i = v / r
    print("current:", i)
    # Check if current exceeds the 2A
    if i > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
