from collections import deque

names = input().split(' ')
step = int(input())
names_queue = deque(names)
counter = 0
while len(names_queue) > 1:
    counter += 1
    current_player = names_queue.popleft()
    if counter == step:
        print(f'Removed {current_player}')
        counter = 0
    else:
        names_queue.append(current_player)
print(f'Last is {names_queue.popleft()}')