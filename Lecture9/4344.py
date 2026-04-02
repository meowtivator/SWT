import sys

input = sys.stdin.readline

for _ in range(int(input())):
    count, *scores = map(int, input().split())
    avg = sum(scores) / count
    result = sum(score > avg for score in scores)
    print(f"{result / count * 100:.3f}%")
