# Ask how many resisters
numofresistors = int(input("how many resistor "))

if numofresistors <= 0:
    print("The number of resistors must be greater than zero.")
else:
    rtotal = 0.0
    res = 0.0
    
    #for loop used to ask resistnace of each resistance and add to r total
    for i in range(1, numofresistors + 1):
        res= float(input(f"R{i}:"))
        rtotal = rtotal + res
        
    # Print the final total resistance
    print("Total resistance:",rtotal,"ohms")
