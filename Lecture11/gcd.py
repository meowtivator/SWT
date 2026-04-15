def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


a, b = map(int, input().split())
print(f"{a}, {b}의 gcd {gcd(a,b)}")
