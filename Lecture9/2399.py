n = int(input())
nums = sorted(list(map(int, input().split())))

prefix_sum = 0
pair_sum = 0
for i, x in enumerate(nums):
    pair_sum += x * i - prefix_sum
    prefix_sum += x

print(pair_sum * 2)
