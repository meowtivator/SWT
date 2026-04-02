num = int(input())

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

offset = sum(days_in_month[: num - 1]) + 4
start_day = offset % 7

print(f"\t  {num}월")
print("일 월 화 수 목 금 토")
print("   " * start_day, end="")

for i in range(1, days_in_month[num - 1] + 1):
    print(f" {i:2d}", end="")
    if (i + start_day) % 7 == 0:
        print()

print()
