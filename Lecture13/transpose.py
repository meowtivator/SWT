import random


def fill_random(n):
    upper = n * n * 10
    return [[random.randint(1, upper - 1) for _ in range(n)] for _ in range(n)]


def pretty_print(mat):
    n = len(mat)
    width = max(len(str(v)) for row in mat for v in row)
    for row in mat:
        print(" ".join(f"{v:>{width}}" for v in row))


def transpose(mat):
    n = len(mat)
    return [[mat[j][i] for j in range(n)] for i in range(n)]


while True:
    n = int(input("N (1 < N <= 5) 입력: "))
    if 1 < n <= 5:
        break
    print("범위를 벗어났습니다.")

A = fill_random(n)

print("A =")
pretty_print(A)

print("A^T =")
pretty_print(transpose(A))
