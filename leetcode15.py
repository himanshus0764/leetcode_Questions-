arr = [0,1,1]
arr2 = []
for i in range(len(arr) - 2):
    for j in range(i + 1, len(arr) - 1):
        for k in range(j + 1, len(arr)):
            if arr[i] + arr[j] + arr[k] == 0:
                new = sorted([arr[i], arr[j], arr[k]])
                if new not in arr2:
                    arr2.append(new)

print(arr2)
