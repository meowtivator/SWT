import sys

input = sys.stdin.readline

counts = {}
n = int(input())

for num in map(int, input().split()):
    counts[num] = counts.get(num, 0) + 1

m = int(input())
result = []
for num in map(int, input().split()):
    result.append(str(counts.get(num, 0)))

print(" ".join(result))
