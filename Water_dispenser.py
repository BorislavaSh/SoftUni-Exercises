from collections import deque

water_litres = int(input())

Start_command = "Start"
End_command = "End"
Refill_command = "refill"
names = deque()

while True:
    command = input()
    if command == Start_command:
        break
    names.append(command)

while True:
    command = input()
    if command == End_command:
        print(f'{water_litres} liters left')
        break
    if command.startswith(Refill_command):
        command_params = command.split(' ')
        refill_liters = int(command_params[1])
        water_litres += refill_liters
    else:
        person = names.popleft()
        person_liters = int(command)
        if person_liters <= water_litres:
            print(f'{person} got water')
            water_litres -= person_liters
        else:
            print(f'{person} must wait')