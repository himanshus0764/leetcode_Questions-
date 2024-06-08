s = "abccccdd"
result = 0
charcount = {}

for char in s:
    if char in charcount:
        charcount[char] += 1
    else:
        charcount[char] = 1

for count in charcount.values():
    result += (count // 2) * 2
    if result % 2 == 0 and count % 2 == 1:
        result += 1

print(result)