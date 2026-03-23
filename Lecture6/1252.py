import sys

a, b = sys.stdin.readline().split()
total = int(a, 2) + int(b, 2)
print(bin(total)[2:])
