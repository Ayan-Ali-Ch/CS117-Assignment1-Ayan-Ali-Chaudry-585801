readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

#Initializing variables
above = 0
totalsum = 0.0
count = 0
highest = 0
lowest = 0

for r in readings:
    totalsum += r
    count += 1
    
    #readings above 3.2 V
    if r > 3.2:
        above += 1
        
    #Track the highest reading
    if r > highest:
        highest = r
        
    #Track the lowest reading
    if r < lowest:
        lowest = r

#Calculate the average reading
average = totalsum / count

# Print the results
print(f"(a) Readings above 3.2 V: {above}")
print(f"(b) Highest reading: {highest} V")
print(f"(c) Lowest reading: {lowest} V")
print(f"(d) Average reading: {average:} V")
