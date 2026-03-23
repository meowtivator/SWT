people = 0
result = 0
for _ in range(4):
    a, b = map(int, input().split())
    people -= a
    people += b
    result = max(people, result)
print(result)
