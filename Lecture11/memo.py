memo = {}
counter = 0
counter2 = 0


def fibo(n):
    global counter
    counter += 1
    if n in memo:
        return memo[n]

    if n == 0:
        memo[0] = 0
    elif n == 1:
        memo[1] = 1
    else:
        memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]


def fibo_legacy(n):
    global counter2
    counter2 += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_legacy(n - 1) + fibo_legacy(n - 2)


n = int(input())
print(f"fibo({n}) = {fibo(n)}")
print(f"fibo({n}) 호출 횟수 = {counter}")

print(f"fibo({n}) = {fibo_legacy(n)}")
print(f"fibo({n}) 호출 횟수 = {counter2}")
