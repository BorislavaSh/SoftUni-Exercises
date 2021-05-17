n_commands = int(input())
users = {}

for i in range(n_commands):
    command = input()

    if 'unregister' in command:
        unregister, username = command.split()
        if username not in users:
            print(f'ERROR: user {username} not found')
        else:
            users.pop(username)
            print(f'{username} unregistered successfully')
    else:
        register, username, license_plate = command.split()
        if username not in users:
            users[username] = license_plate
            print(f'{username} registered {license_plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {license_plate}')

for username, plate in users.items():
    print(f'{username} => {plate}')