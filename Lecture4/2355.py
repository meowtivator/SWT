import sys

input = sys.stdin.readline


def ADD(A, B):
    a = abs(A)
    b = abs(B)
    return (a + b) * (b - a + 1) // 2


A, B = sorted(map(int, input().split()))

if A < 0 and B < 0:
    print(-1 * ADD(B, A))
elif A > 0 and B > 0:
    print(ADD(A, B))
else:
    print(ADD(A - 1, B))
