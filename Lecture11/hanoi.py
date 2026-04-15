def hanoi(n, start, mid, end):
    if n == 0:
        return
    hanoi(n - 1, start, end, mid)
    print(f"{n}: {start} -> {end}")
    hanoi(n - 1, mid, start, end)


n = int(input())
hanoi(n, "a", "b", "c")
