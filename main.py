list = [0, 1, 0, 12, 3]
nonzeros = []
zeros = []

for element in range(len(list)):
    if list[element] !=0:
        nonzeros.append(list[element])
    else:
        zeros.append(list[element])

print(nonzeros+zeros)


list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 96, 0]
nonzeros = []
zeros = []

for element in range(len(list)):
    if list[element] !=0:
        nonzeros.append(list[element])
    else:
        zeros.append(list[element])

print(nonzeros+zeros)