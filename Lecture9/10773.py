moneys = []
for _ in range(int(input())):
    money = int(input())
    if money == 0:
        moneys.pop()
    else:
        moneys.append(money)

print(sum(moneys))
