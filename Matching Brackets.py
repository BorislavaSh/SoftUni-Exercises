data = input()
s = []

for i in range(len(data)):
    ch = data[i]
    if ch == "(":
        s.append(i)
    elif ch == ")":
        j = s.pop()
        print(data[j:i + 1])