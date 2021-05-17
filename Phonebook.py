phonebook = {}

while True:
    numbers = input()
    if numbers.isnumeric():
        break
    name, number = numbers.split("-")
    phonebook[name] = number

n = int(numbers)
for _ in range(n):
    contact = input()
    if contact not in phonebook:
        print(f'Contact {contact} does not exist.')
    else:
        print(f'{contact} -> {phonebook[contact]}')