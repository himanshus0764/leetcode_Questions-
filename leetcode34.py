nums = [5, 7, 7, 8, 8, 10]
target = 8
high = len(nums) - 1
low = 0
leftmost = -1
rightmost = -1

# Finding leftmost occurrence
while low <= high:
    mid = low + (high - low) // 2
    if nums[mid] == target:
        leftmost = mid
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

low = 0
high = len(nums) - 1

# Finding rightmost occurrence
while low <= high:
    mid = low + (high - low) // 2
    if nums[mid] == target:
        rightmost = mid
        low = mid + 1
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

print("[", leftmost if leftmost != -1 else -1, ",", rightmost if rightmost != -1 else -1, "]")
