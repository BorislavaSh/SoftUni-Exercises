n_symbols = int(input())

symbols = set()

for _ in range(n_symbols):
    name = input().split()
    for i in name:
        symbols.add(i)

for n in symbols:
    print(n)