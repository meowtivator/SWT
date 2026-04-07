sales = {}
for _ in range(int(input())):
    book = input()
    sales[book] = sales.get(book, 0) + 1

result = min(sales.items(), key=lambda x: (-x[1], x[0]))[0]
print(result)
