data = input()

chara = {}

for ch in data:
    if ch not in chara:
        chara[ch] = 0
    chara[ch] += 1

chara = dict(sorted(chara.items()))

for char, count in chara.items():
    print(f'{char}: {count} time/s')