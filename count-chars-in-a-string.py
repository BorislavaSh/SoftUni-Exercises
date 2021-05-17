words = input().split()
chars_count = {}

for i in words:
    for char in i:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count.update({char: 1})

for char, occurrences in chars_count.items():
    print(f'{char} -> {occurrences}')