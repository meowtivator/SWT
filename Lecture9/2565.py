import sys

nums = list(map(int, sys.stdin.read().split()))
print(max(nums))
print(nums.index(max(nums)) + 1)
