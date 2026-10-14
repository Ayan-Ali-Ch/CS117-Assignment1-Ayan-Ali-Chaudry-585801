# ask user for color and convert it to lower case with lower() code
colour = input("Enter the colour of the first band: ").lower()

# Check the colour and print the assigned digit
if colour == "black":
    print(0)
elif colour == "brown":
    print(1)
elif colour == "red":
    print(2)
elif colour == "orange":
    print(3)
elif colour == "yellow":
    print(4)
elif colour == "green":
    print(5)
elif colour == "blue":
    print(6)
elif colour == "violet":
    print(7)
elif colour == "grey":
    print(8)
elif colour == "white":
    print(9)
else:
    print("Invalid colour")
