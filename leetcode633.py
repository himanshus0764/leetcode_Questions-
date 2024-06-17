import math

c = 2
result = False
for a in range(int(math.sqrt(c)) + 1):
    b_squared = c - a ** 2
    if b_squared >= 0:
        b = int(b_squared ** 0.5)
        if b * b == b_squared:
            result = True
            break