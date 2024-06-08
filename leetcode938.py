root = [10, 5, 15, 3, 7, 13, 18, 1, 0, 6]
low = 7
high = 15
result = 0
result = 0
stack = [root]
while stack:
    node = stack.pop()
    if low <= node.val <= high:
        result += node.val
    if node.left:
        stack.append(node.left)
    if node.right:
        stack.append(node.right)
print(result)