import sys

input = sys.stdin.readline

k, l = map(int, input().split())
wait = {}

for _ in range(l):
    student = input().strip()
    if student in wait:
        del wait[student]
    wait[student] = None

print("\n".join(list(wait.keys())[:k]))
