for _ in range(int(input())):
    elements = input().split("X")
    sum = 0
    for e in elements:
        length = len(e)
        sum += (length + 1) * (length) // 2
    print(sum)
