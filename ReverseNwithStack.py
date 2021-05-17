numbers = input().split(" ")

s = []

for i in numbers:
    s.append(i)

result = " "
while s:
    result = s.pop()
    print(result, end=" ")
