n = int(input())
row_count = 1 if n == 1 else n * 2
odd_row = "".join("*" if index % 2 else " " for index in range(1, n + 1)).rstrip()
even_row = "".join(" " if index % 2 else "*" for index in range(1, n + 1)).rstrip()

for row in range(row_count):
    print(odd_row if row % 2 == 0 else even_row)
