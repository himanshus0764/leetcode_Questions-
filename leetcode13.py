n = input()

store = 0
arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ar = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

i = 0

while n:
    if n.startswith(ar[i]):
        store += arr[i]
        n = n[len(ar[i]):]
    else:
        i += 1
        if i >= len(ar):
            break

print(store)
