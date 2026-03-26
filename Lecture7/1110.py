original = input().zfill(2)
current = original
count = 0

while True:
    digit_sum = int(current[0]) + int(current[1])
    current = current[1] + str(digit_sum % 10)
    count += 1

    if current == original:
        break

print(count)
