a, b = map(int, input().split())
result = 0
for i in range(1, b + 1):
    result = max(result, int(str(i * a)[::-1]))

print(result)
