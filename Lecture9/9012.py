for _ in range(int(input())):
    stack = []
    for ch in input().strip():
        if ch == "(":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break

    else:
        print("YES" if not stack else "NO")
