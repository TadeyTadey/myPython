#finding the biggest value
largest = -1

for i in [9, 40, 1, 34, 55, 2, 33]:
    if i > largest:
        largest = i

print(largest)

#Finding the smallest value 
largest = None
for i in [9, 40, 1, 34, 55, 2, 33]:
    if largest is None:             # is - use only for None or True/False
        largest = i
    elif i < largest:
        largest = i

print(largest)