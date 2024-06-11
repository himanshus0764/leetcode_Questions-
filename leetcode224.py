stack = []
num = 0
sign = 1
result = 0

for char in s:
    if char.isdigit():
        num = num * 10 + int(char)
    elif char in ['+', '-']:
        result += sign * num
        num = 0
        sign = 1 if char == '+' else -1
    elif char == '(':
        stack.append(result)
        stack.append(sign)
        result = 0
        sign = 1
    elif char == ')':
        result = stack.pop() * result + stack.pop()
result += sign * num
