A = set()
B = set()

N, M = map(int, input().split())
for _ in range(N):
    A.add(input().strip())
for _ in range(M):
    B.add(input().strip())

result = A & B
print(len(result))
print("\n".join(sorted(result)))
