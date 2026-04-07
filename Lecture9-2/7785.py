peoples = set()
for _ in range(int(input())):
    name, state = input().split()
    if state == "enter":
        peoples.add(name)
    else:
        peoples.remove(name)

print("\n".join(sorted(peoples, reverse=True)))
