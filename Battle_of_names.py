n = int(input())

odd_s = set()
even_s = set()

for line in range(1, n + 1):
    name = input()
    val_sum = 0
    for ch in name:
        value = ord(ch)
        val_sum += value
    val_sum //= line
    if val_sum % 2 == 0:
        even_s.add(val_sum)
    else:
        odd_s.add(val_sum)

even_sum = sum(even_s)
odd_sum = sum(odd_s)

if odd_sum == even_sum:
    result = tuple(odd_s.union(even_s))
    print(', '.join(map(str, result)))
elif odd_sum > even_sum:
    result = tuple(odd_s.difference(even_s))
    print(', '.join(map(str, result)))
    pass
elif odd_sum < even_sum:
    result = tuple(odd_s.symmetric_difference(even_s))
    print(', '.join(map(str, result)))