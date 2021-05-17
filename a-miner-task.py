keys = []
values = []
count = 0

while True:
    word = input()
    count += 1
    if word == 'stop':
        break
    if count % 2 == 0:
        values.append(word)
    else:
        if word in keys:
            added = keys.index(word)
            value = input()
            count += 1
            values[added] = str(int(values[added]) + int(value))
        else:
            keys.append(word)

resources = dict(zip(keys, values))

for resource in resources:
    print(f"{resource} -> {resources[resource]}")

