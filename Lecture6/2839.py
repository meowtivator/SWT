n = int(input())
m = n // 5

for i in range(m, -1, -1):
    remain = n - 5 * i
    if remain % 3 == 0:
        print(i + remain // 3)
        break
else:
    print(-1)
