def d(n):
    total = n
    for s in str(n):
        total += int(s)

    return total


a = [True] * 10001

for i in range(1, 10001):
    x = d(i)
    if x <= 10000:
        a[x] = False

for i in range(1, 10001):
    if a[i]:
        print(i)
