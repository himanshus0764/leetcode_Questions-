arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
result=[]
v=[]
for i in arr2:
    for j in range(len(arr1)):
        if arr1[j] == i:
            result.append(arr1[j])
print(result)
for i in arr1:
    if i not in result:
        v.append(i)
result.extend(sorted(v))
print(result)
