import sys


binary = sys.stdin.readline().strip()
octal_map = {
    "000": "0",
    "001": "1",
    "010": "2",
    "011": "3",
    "100": "4",
    "101": "5",
    "110": "6",
    "111": "7",
}

first_group = len(binary) % 3
result = []

if first_group:
    result.append(str(int(binary[:first_group], 2)))

for index in range(first_group, len(binary), 3):
    result.append(octal_map[binary[index : index + 3]])

print("".join(result) or "0")
