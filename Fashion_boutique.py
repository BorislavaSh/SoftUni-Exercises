sequence = input()

stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
}

success = True
for el in sequence:
    if el in pairs.values():
        stack.append(el)
    elif el in pairs.keys():
        if not stack:
            success = False
            break
        opening = stack.pop()
        if not opening == pairs[el]:
            success = False
            break

if success:
    print('YES')
else:
    print('NO')