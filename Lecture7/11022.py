n = int(input())
for x in range(1, n + 1):
    A, B = map(int, input().split())
    print(f"Case #{x}: {A} + {B} = {A+B}")
