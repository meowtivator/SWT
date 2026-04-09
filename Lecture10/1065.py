def is_hansu(n):
    if n < 100:
        return True

    s = str(n)
    return int(s[0]) - int(s[1]) == int(s[1]) - int(s[2])


n = int(input())

count = 0
for i in range(1, n + 1):
    if is_hansu(i):
        count += 1

print(count)
