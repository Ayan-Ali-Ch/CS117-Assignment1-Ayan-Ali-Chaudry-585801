# Get three resistor values from the user
r1 = float(input("Enter first resistor value: "))
r2 = float(input("Enter second resistor value: "))
r3 = float(input("Enter third resistor value: "))

# code for finding largest
if r1 >= r2 and r1 >= r3:
    largest = r1
elif r2 >= r1 and r2 >= r3:
    largest = r2
else:
    largest = r3
# code for finding smallest
if r1 <= r2 and r1 <= r3:
    smallest = r1
elif r2 <= r1 and r2 <= r3:
    smallest = r2
else:
    smallest = r3
#pinting results
print("Smallest resistor:",smallest)
print("Largest resistor:",largest)
