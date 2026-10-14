#defining functions
def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return (i ** 2) * r

# input values
voltage = float(input("input voltage:"))
resistance = float(input("input resistance:"))

# Calling functions
current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)
i=current
print(f"Current = {current} A")
print(f"Power = {power} W")
