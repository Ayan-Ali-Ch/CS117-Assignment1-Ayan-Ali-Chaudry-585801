#initializing
count_1 = 0
count_5 = 0
count_reject = 0
while True:
    measured = float(input("Enter resistance (0 to stop): "))
#code to stop if zero and counter to increase if within parameter
    if measured == 0:
        break
        
    if 99.0 <= measured <= 101.0:
        count_1 += 1
    elif 95.0 <= measured <= 105.0:
        count_5 += 1
    else:
        count_reject += 1

print("1% tolerance:", count_1)
print("5% tolerance:", count_5)
print("Reject:", count_reject)
