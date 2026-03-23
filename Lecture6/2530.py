h, m, s = map(int, input().split())
add_seconds = int(input())

total_seconds = (h * 3600 + m * 60 + s + add_seconds) % (24 * 3600)

h = total_seconds // 3600
m = (total_seconds % 3600) // 60
s = total_seconds % 60

print(h, m, s)
