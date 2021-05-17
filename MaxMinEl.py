def Push(value):
    # takes the value and adds it to the stack
    value = value.split(" ")
    n = value[1]
    s.append(int(n))
    return s


def Delete():
    # deletes the top value
    s.pop()
    return s


def PrintMax():
    # prints the max value in the stack
    print(max(s))


def PrintMin():
    # prints the min value in the stack
    print(min(s))


s = []
data = int(input())

for i in range(data):
    query = input()
    if query.startswith("1"):
        Push(query)
    elif query.startswith("2"):
        if len(s) == 0:
            pass
        else:
            Delete()
    elif query.startswith("3"):
        if len(s) == 0:
            pass
        else:
            PrintMax()
    elif query.startswith("4"):
        if len(s) == 0:
            pass
        else:
            PrintMin()

result = []
while s:
    result.append(s.pop())

print(*result, sep=", ")