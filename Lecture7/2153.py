def is_prime(number):
    if number == 1:
        return True
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for divisor in range(3, int(number**0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True


word = input().strip()
score = 0

for ch in word:
    if "a" <= ch <= "z":
        score += ord(ch) - 96
    else:
        score += ord(ch) - 38

if is_prime(score):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
