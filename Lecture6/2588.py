a, b = [int(input()) for _ in range(2)]
result = a * b
print(a * (b % 10))
print(a * (b % 100 // 10))
print(a * (b // 100))
print(result)
