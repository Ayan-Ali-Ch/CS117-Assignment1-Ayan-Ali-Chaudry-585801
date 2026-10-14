def parallel_resistance(resistors):
    inv_sum = 0
    for r in resistors:
        inv_sum += 1 / r
    return 1 / inv_sum

resistor_list = []
print("Enter resistor values one by one. Enter 0 when finished.")
while True:
    try:
        val = float(input("Enter resistor value (ohms): "))
        if val == 0:
            break
        resistor_list.append(val)
    except ValueError:
        print("Please enter a valid value.")

# Calling the function
result = parallel_resistance(resistor_list)
print(f"parallel resistance({resistor_list}):{result}")
