words = input().split(" ")
result = [word for word in words if len(word) % 2 == 0]

print(*result, sep="\n")