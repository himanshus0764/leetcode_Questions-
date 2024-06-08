n = int(input("Enter a number: "))

store = ""
arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ar = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

i = 0

while n > 0:
    if n >= arr[i]:
        n -= arr[i]
        store += ar[i]
    else:
        i += 1

print(store)
