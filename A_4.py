# ask user for 2 bits
a = int(input("Enter bit A: "))
b = int(input("Enter bit B: "))

# check if a and b is 1 or 0
if a not in (0, 1) or b not in (0, 1):
    print("Bits must be 0 or 1")
else:
    #outputs
    andoutput = a and b
    oroutput = a or b
    if a != b:
        xoroutput=1
    else:
        xoroutput=0


# Print the results
print("AND:",andoutput)
print("OR:",oroutput)
print("XOR:",xoroutput)
