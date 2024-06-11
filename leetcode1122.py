arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
count_dict = {}
newarr = []

for element in arr1:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1

for element in arr2:
    if element in count_dict:
        newarr.extend([element] * count_dict[element])
        del count_dict[element]
a = sorted(count_dict)
newarr.extend(a)

print(newarr)

