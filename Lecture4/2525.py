a, b = map(int, input().split())
c = int(input())

counter = 0
while c > 0:
    b = b + c - 60
    counter += 1
    c -= 60
a = a + counter if a + counter >= 24 else a

print(f"{a} {b}")
