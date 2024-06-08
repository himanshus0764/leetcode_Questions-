words = ["bella", "label", "roller"]
lol = {}
for word in words:
    for char in word:
        if char in lol:
            lol[char] += 1
        else:
            lol[char] = 1
lol = [(char, count) for char, count in lol.items()]
print(lol)
