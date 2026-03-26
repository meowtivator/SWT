n, x = map(int, input().split())
for a in list(map(int, input().split())):
    if a < x:
        print(a, end=" ")
