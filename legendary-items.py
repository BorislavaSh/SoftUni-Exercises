materials = input().lower().split()
legendary_items = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_materials = {}
obtained = False

while True:
    for i in range(0, len(materials), 2):
        key = materials[i + 1]
        value = int(materials[i])
        if key in legendary_items:
            legendary_items[key] += value
        elif key in junk_materials:
            junk_materials[key] += value
        elif key not in legendary_items and key in ('shards', 'fragments', 'motes'):
            legendary_items[key] = value
        else:
            junk_materials[key] = value
        if key in ('shards', 'fragments', 'motes') and legendary_items[key] >= 250:
            legendary_items[key] -= 250
            if key == 'shards':
                print('Shadowmourne obtained!')
            elif key == 'fragments':
                print('Valanyr obtained!')
            elif key == 'motes':
                print('Dragonwrath obtained!')
            obtained = True
            break
    if obtained:
        break
    materials = input().lower().split()

legendary_items = dict(sorted(legendary_items.items(), key= lambda s: (-s[1], s[0])))
junk = dict(sorted(junk_materials.items(), key= lambda s: s[0]))

for key, value in legendary_items.items():
    print(f'{key}: {value}')
for key, value in junk.items():
    print(f'{key}: {value}')